import streamlit as st

st.title("Workshop agenda")

AGENDA = [
    ("9:00 - 9:10 AM", "Arrival & Coffee", None, None),
    ("9:10 - 9:15 AM", "Welcome & Workshop Overview", None, None),
    ("9:15 - 9:30 AM", "Session 1: Data Prep", "15 min", "1"),
    ("9:30 - 9:55 AM", "Session 2: Cortex Analyst & Semantic Views", "25 min", "2"),
    ("9:55 - 10:15 AM", "Session 3: Cortex Search", "20 min", "3"),
    ("10:15 - 10:25 AM", ":orange-badge[BREAK]", None, None),
    ("10:25 - 10:40 AM", "Session 4: Cortex Agents", "15 min", "4"),
    ("10:40 - 10:50 AM", "Session 5: CoWork", "10 min", "5"),
    ("10:50 - 11:00 AM", "Session 6: Streamlit", "10 min", "6"),
]

for time, title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f"{title}")
    else:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":gray[{title}]")

st.space("medium")

st.markdown("##### What you'll build by end of morning")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | 9 | Production records, pipeline throughput, safety incidents, AER inspections |
| **Cortex Search Services** | 1 | Energy knowledge base search |
| **Semantic Views** | 1 | ENERGY_OPERATIONS_VIEW with relationships, metrics, and AI instructions |
| **Cortex Agents** | 1 | Energy operations agent with Analyst + Search + custom tools |
| **Streamlit Apps** | 1 | Operations dashboard with AI chat |
""")

st.space("small")

st.markdown("##### Location")
with st.container(border=True):
    st.markdown("""
:material/location_on: **The Ampersant, Calgary, AB**

July 16, 2026 — 9:00 AM to 11:00 AM
""")
