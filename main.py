import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Match Tracker", layout="centered")

st.title("🏏 IPL Match Tracker")

# IPL teams
team_names = ["CSK", "MI", "KKR", "SRH", "RCB", "GT"]

# Initialize session state
if 'points_table' not in st.session_state:
    st.session_state.points_table = {team: 0 for team in team_names}
if 'match_history' not in st.session_state:
    st.session_state.match_history = []

# Match input form
st.subheader("Enter Match Result")

col1, col2 = st.columns(2)
team1 = col1.selectbox("Team 1", team_names)
team2 = col2.selectbox("Team 2", [team for team in team_names if team != team1])

# Dynamically update winner options
if team1 and team2:
    winner = st.radio("Select Winner", [team1, team2])
else:
    winner = None

if st.button("Submit Match") and winner:
    # Add match to history
    match = {
        "Team 1": team1,
        "Team 2": team2,
        "Winner": winner
    }
    st.session_state.match_history.append(match)

    # Update points
    st.session_state.points_table[winner] += 2
    st.success(f"{winner} won! 2 points added.")

# Display Points Table
st.subheader("🏆 Points Table")
points_df = pd.DataFrame.from_dict(st.session_state.points_table, orient='index', columns=['Points'])
points_df = points_df.sort_values(by='Points', ascending=False)
st.table(points_df)

# Display Match History
st.subheader("📜 Match History")
if st.session_state.match_history:
    history_df = pd.DataFrame(st.session_state.match_history)
    st.dataframe(history_df)
else:
    st.info("No matches played yet.")
