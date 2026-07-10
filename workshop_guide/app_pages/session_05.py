import streamlit as st
from components import render_session_header, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(5, "CoWork", "10:40 - 10:50 AM", "10 min", "Collaborative AI analysis with CoWork")

render_technologies_used([
    {"name": "Snowflake CoWork", "description": "An AI-powered collaborative workspace inside Snowsight where you can analyze data, generate insights, and share findings with your team.", "icon": "group"},
    {"name": "Data Analysis", "description": "CoWork can query your Snowflake data, generate visualizations, and provide insights without writing SQL.", "icon": "analytics"},
    {"name": "Sharing & Collaboration", "description": "CoWork sessions can be shared with team members for collaborative data exploration.", "icon": "share"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open CoWork")
with st.container(border=True):
    st.markdown("""
In Snowsight, click **CoWork** in the left navigation panel. Start a new conversation.

CoWork discovers your tables in `ENERGY_AI.OPS` automatically. Paste each question below one at a time and observe how it generates queries and visualizations.
""")

st.space("small")

st.markdown("#### :material/chat: Questions to ask CoWork")
st.caption("Copy and paste each question into CoWork individually.")

questions = [
    ("1. Operations Overview", "Show me an overview of Alberta energy operations — total production volume, number of active facilities, and average pipeline utilization rate."),
    ("2. Production Trends", "Create a visualization showing production volume by facility and product type. Which facilities are the largest producers?"),
    ("3. Pipeline Performance", "Compare pipeline utilization rates across the network. Which pipelines are running closest to capacity?"),
    ("4. Safety Analysis", "What are the most common safety incident categories? Show a breakdown by severity and facility."),
    ("5. Efficiency Metrics", "What is the average steam-oil ratio by facility? Which SAGD operations are most efficient?"),
    ("6. Recommendations", "Based on the production data, pipeline utilization, and safety incidents, what are the top 3 operational risks and recommendations?"),
]

for title, question in questions:
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.code(question, language="text", wrap_lines=True)

st.space("small")

render_explanation("How CoWork works", """
**CoWork** is Snowflake's collaborative AI workspace — different from Cortex Code:

| Tool | Best for |
|------|----------|
| Cortex Code | Building infrastructure, creating objects, writing SQL |
| CoWork | Exploring data, generating insights, team collaboration |
| Cortex Agent | End-user Q&A interface (deployed as a product) |
""")

render_key_concepts([
    {"term": "CoWork", "definition": "Snowflake's collaborative AI workspace. Conversational interface that queries data, creates visualizations, and generates insights without requiring SQL."},
    {"term": "Context Maintenance", "definition": "CoWork maintains conversation history so follow-up questions build on previous analysis."},
])

render_what_you_built([
    "Explored energy operations data through conversational AI",
    "Generated visualizations and cross-table analysis",
    "Demonstrated the CoWork collaborative analysis pattern",
])
