import streamlit as st

st.title("Alberta Energy Operations AI Workshop")
st.markdown("Building Intelligence for Canada's Energy Sector with Snowflake Cortex")

st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Prompts", "16", help="Total prompts across all tools")
col3.metric("Duration", "2 hrs", help="Total workshop time")

st.space("medium")

st.markdown("#### How this workshop works")

st.markdown("""
Each section has **numbered prompts** that you copy and paste into the appropriate tool:

- **Cortex Code** — for building infrastructure, creating objects, and writing SQL/Python
- **Cortex Analyst** — for testing natural language queries against your semantic view
- **Snowflake CoWork** — for collaborative data exploration and analysis

All prompts build on each other sequentially — run them in order throughout the morning.
""")

st.space("small")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
**Alberta's oil sands and pipeline network** represent one of the world's largest energy operations,
producing over **3.5 million barrels per day** and transporting crude via an extensive pipeline
network to refineries across North America. Operators must manage production optimization, pipeline
integrity, environmental compliance, and safety across remote and complex operations.

We'll build a complete AI platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | Production records, pipeline throughput, transport invoices, facility data |
| **Unstructured** | AER inspection reports, environmental reports, safety incident logs |
| **Time series** | Pipeline throughput metrics, SAGD well monitoring data |
""")

st.space("small")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In 2 hours, we build a complete AI-powered operations platform:

**1. Data Foundation** — Load structured and unstructured energy operations data into Snowflake from pre-generated CSV files.

**2. Natural Language Analytics** — Create a Semantic View over operational tables and query them with plain English via Cortex Analyst.

**3. Intelligent Search** — Build a Cortex Search service over safety incidents, environmental reports, and AER inspections for hybrid semantic + keyword search.

**4. AI Agents** — Create a Cortex Agent that orchestrates structured data queries AND document search through a single conversational interface.

**5. Collaborative AI** — Use CoWork to collaboratively analyze energy operations data with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and an AI chat interface.
""")

st.space("small")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.space("medium")
st.caption("Built for the July 16, 2026 workshop  :material/location_on:  The Ampersant, Calgary, AB")
