import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, "Cortex Agents", "10:25 - 10:40 AM", "15 min", "Cortex Agent with Analyst + Search + custom tools")

render_technologies_used([
    {"name": "Cortex Agent (CREATE AGENT)", "description": "An orchestrating AI that plans tasks, selects tools, executes them, reflects on results, and generates responses. Created as a first-class Snowflake object.", "icon": "smart_toy"},
    {"name": "Tool Orchestration", "description": "The Agent automatically routes questions to the right tool: Cortex Analyst for structured data, Cortex Search for unstructured documents, custom UDFs for business logic.", "icon": "route"},
    {"name": "Custom Tools (UDFs)", "description": "User-defined functions that extend Agent capabilities with custom business logic and calculations.", "icon": "build"},
])


PROMPT_4_1 = """In ENERGY_AI.OPS, create a Cortex Agent called ENERGY_OPS_AGENT.

It should:
- Use auto as the orchestration model
- Have two tools: the ENERGY_OPERATIONS_VIEW semantic view (for structured data queries) and the energy_knowledge_search Cortex Search service (for safety/environmental/regulatory docs)
- Include instructions defining it as the Alberta Energy Operations Assistant, guiding it to use structured data for production/pipeline/financial questions and search for incidents/compliance/environmental questions
- Mention domain context: Alberta oil sands operations, AER is the regulator, SAGD extraction, pipeline network serving North American refineries, key operators (CNRL, Cenovus, Imperial, TC Energy, Shell)
- Include 3-4 sample questions spanning both tools

Execute and show confirmation."""

render_prompt("Prompt 4.1", "Create the Cortex Agent", PROMPT_4_1)

render_explanation("What this prompt does", """
Creates a **Cortex Agent** that combines structured data analytics with document search:

- **Structured questions** (production volumes, pipeline utilization, transport values) → routed to Cortex Analyst via the semantic view
- **Unstructured questions** (safety incidents, AER compliance, environmental reports) → routed to Cortex Search
- **Mixed questions** → Agent uses both tools and synthesizes results
""")


PROMPT_4_2 = """Test our ENERGY_OPS_AGENT with these queries:

1. Structured: "What is the total production volume by operator and what are their average pipeline utilization rates?"
2. Unstructured: "Have there been any H2S incidents or pipeline integrity issues? What were the causes and resolutions?"
3. Mixed: "Which facilities have the highest production volumes AND the most safety incidents? Is there a correlation between production intensity and incident frequency?"

Show the responses and note which tools the agent selected."""

render_prompt("Prompt 4.2", "Test the Agent", PROMPT_4_2)

render_explanation("What this prompt does", """
Tests three query types:

1. **Pure structured** — Agent routes to Analyst, generates SQL joining production_records and pipeline_throughput
2. **Pure unstructured** — Agent routes to Search, retrieves H2S and pipeline incident documents
3. **Mixed** — Agent uses BOTH tools: Analyst for production volumes, Search for safety incidents, then correlates
""")


PROMPT_4_3 = """In ENERGY_AI.OPS, add a custom tool to the agent:

1. Create a UDF that assesses pipeline risk:

CREATE OR REPLACE FUNCTION ENERGY_AI.OPS.ASSESS_PIPELINE_RISK(
    pipeline_name VARCHAR,
    utilization_pct NUMBER,
    age_years NUMBER
)
RETURNS VARIANT
LANGUAGE SQL
AS
$$
    SELECT OBJECT_CONSTRUCT(
        'pipeline', pipeline_name,
        'utilization_pct', utilization_pct,
        'age_years', age_years,
        'risk_level',
            CASE
                WHEN age_years > 25 AND utilization_pct > 85 THEN 'HIGH'
                WHEN age_years > 25 OR utilization_pct > 85 THEN 'MEDIUM'
                ELSE 'LOW'
            END,
        'recommendation',
            CASE
                WHEN age_years > 25 AND utilization_pct > 85 THEN 'Schedule inline inspection and consider capacity expansion or pressure reduction'
                WHEN age_years > 25 OR utilization_pct > 85 THEN 'Increase monitoring frequency and plan integrity assessment'
                ELSE 'Standard operations and monitoring'
            END
    )
$$;

2. Recreate ENERGY_OPS_AGENT with ASSESS_PIPELINE_RISK as an additional tool.

3. Test with: "What is the risk assessment for a pipeline running at 92% utilization that was commissioned 30 years ago?"

Execute all SQL."""

render_prompt("Prompt 4.3", "Agent with Custom Tool", PROMPT_4_3)

render_explanation("What this prompt does", """
Adds a **custom UDF tool** for pipeline risk assessment. The Agent can now:
- Query structured data (Analyst)
- Search documents (Search)  
- Calculate risk scores (custom UDF)

The risk model considers pipeline age and utilization — both key factors in pipeline integrity management under CER and AER regulations.
""")


render_key_concepts([
    {"term": "Cortex Agent", "definition": "A Snowflake object that orchestrates LLMs, Analyst, Search, and custom tools. Plans, executes, reflects, and generates responses for complex questions."},
    {"term": "Tool Routing", "definition": "The Agent selects the right tool for each question. Production data → Analyst. Safety documents → Search. Risk calculations → custom UDF."},
    {"term": "Custom Tools", "definition": "SQL UDFs registered as Agent tools. Enable domain-specific calculations like pipeline risk scoring, production forecasting, or compliance checking."},
])

render_what_you_built([
    "ENERGY_OPS_AGENT — Cortex Agent with Analyst + Search tools",
    "Tested structured, unstructured, and mixed queries",
    "ASSESS_PIPELINE_RISK UDF as a custom tool",
    "Enhanced agent with three tool types",
])
