import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(2, "Cortex Analyst & Semantic Views", "9:30 - 9:55 AM", "25 min", "Semantic view with relationships, metrics, and natural language queries")

render_technologies_used([
    {"name": "Cortex Analyst", "description": "Snowflake's text-to-SQL engine that converts natural language questions into SQL queries using a semantic view to understand your data's business meaning.", "icon": "chat"},
    {"name": "Semantic View", "description": "A first-class Snowflake object (CREATE SEMANTIC VIEW) that describes your data in business terms: tables, relationships, facts, dimensions, metrics, and synonyms.", "icon": "description"},
    {"name": "AI_SQL_GENERATION", "description": "Custom instructions embedded in the semantic view that guide how Cortex Analyst generates SQL — providing domain context, business rules, and disambiguation hints.", "icon": "auto_fix_high"},
])


PROMPT_2_1 = """In ENERGY_AI.OPS, create a semantic view called ENERGY_OPERATIONS_VIEW for use with Cortex Analyst. It should cover these tables: FACILITIES, PIPELINES, PRODUCTION_RECORDS, TRANSPORT_INVOICES, PIPELINE_THROUGHPUT, WELL_MONITORING.

Include:
- Proper relationships between the tables (production_records joins to facilities via facility_id, production_records joins to pipelines via pipeline_id, transport_invoices joins to production_records via record_id, pipeline_throughput joins to pipelines via pipeline_id and facilities via facility_id, well_monitoring joins to facilities via facility_id)
- Facts for key numeric columns: volume_barrels, volume_cubic_meters, api_gravity, sulfur_content_pct, water_cut_pct, royalty_rate_pct, price_per_barrel_cad, total_value_cad, throughput_bpd, pressure_kpa, temperature_celsius, utilization_pct, steam_injection_rate, oil_production_rate, sor_ratio
- Dimensions for categorical columns like product_type, facility_name, pipeline_name, operator, facility_type, pipeline_type, aer_compliance_status, transport_mode, destination_city, status, well_pad, and all date/time columns
- Add useful SYNONYMS (e.g. facility_name could be 'plant' or 'site', pipeline_name could be 'line', product_type could be 'crude type' or 'commodity')
- Metrics: total production volume, average API gravity, total transport value, average pipeline utilization, average SOR (steam-oil ratio), total throughput
- An AI_SQL_GENERATION instruction with domain context: this is Alberta oil sands and pipeline operations data, AER is the Alberta Energy Regulator, SAGD is Steam-Assisted Gravity Drainage, SOR is steam-oil ratio (lower is better), WCS is Western Canadian Select, key operators include CNRL/Cenovus/Imperial/TC Energy/Shell

Execute the SQL and confirm with DESCRIBE SEMANTIC VIEW."""

render_prompt("Prompt 2.1", "Create the Semantic View", PROMPT_2_1)

render_explanation("What this prompt does", """
Creates a **semantic view** — a first-class Snowflake object that enables natural language to SQL for energy operations data.

**Key domain concepts in the view**:
- **SOR (Steam-Oil Ratio)**: Key SAGD efficiency metric — cubic meters of steam per cubic meter of bitumen. Lower is better (2.5 is excellent, 5.0+ is poor).
- **API Gravity**: Density measure — higher = lighter crude. Bitumen is ~8°, synthetic crude ~30-35°.
- **WCS Discount**: Western Canadian Select trades at a discount to WTI benchmark.
- **AER Compliance**: Alberta Energy Regulator status (compliant, under_review, non_compliant).
""")


PROMPT_2_2 = """Ask Cortex Analyst these questions using ENERGY_AI.OPS.ENERGY_OPERATIONS_VIEW:

1. "What is the total production volume by facility and product type?"
2. "Which pipelines have the highest average utilization rate?"
3. "What is the average steam-oil ratio by facility for SAGD operations?"
4. "What are the top destination cities by total transport value?"

Show the generated SQL and results for each."""

render_prompt("Prompt 2.2", "Test with Natural Language Queries", PROMPT_2_2)

st.info("""
:material/lightbulb: **You can also test these in the Cortex Analyst UI!**

In Snowsight, navigate to **AI & ML → Cortex Analyst** in the left sidebar. Select your `ENERGY_OPERATIONS_VIEW` semantic view, and you'll see a playground where you can type natural language questions and see the generated SQL and results interactively.
""")

render_explanation("What this prompt does", """
Tests Cortex Analyst across different energy operations question types:

1. **Production by facility/product** — Tests GROUP BY with two dimensions and SUM aggregation across the core production table.
2. **Pipeline utilization** — Tests AVG metric on pipeline_throughput joined to pipelines.
3. **SOR by facility** — Tests a domain-specific metric (steam-oil ratio) that the AI_SQL_GENERATION instruction helps Analyst understand.
4. **Transport value by destination** — Tests the transport_invoices table with aggregation.
""")


PROMPT_2_3 = """Now expand our ENERGY_OPERATIONS_VIEW in ENERGY_AI.OPS to improve it:

1. Query INFORMATION_SCHEMA.COLUMNS to review what's available
2. Add these additional metrics to the view:
   - Production efficiency (oil_production_rate / steam_injection_rate from WELL_MONITORING)  
   - Non-compliance rate (% of production_records with aer_compliance_status != 'compliant')
   - Pipeline capacity utilization by pipeline (throughput_bpd / max_throughput_bpd)
3. Recreate the view with the additional metrics

Test by asking: "Which facilities have the highest non-compliance rate and what product types are they producing?"

Execute all SQL."""

render_prompt("Prompt 2.3", "Expand the Semantic View", PROMPT_2_3)

render_explanation("What this prompt does", """
Demonstrates iterative semantic view development — adding calculated metrics that combine data from multiple tables.

**Key calculated metrics**:
- **Production efficiency**: Ratio of oil produced to steam injected (higher = more efficient SAGD operation)
- **Non-compliance rate**: Percentage of records flagged by AER — indicates regulatory risk
- **Capacity utilization**: How full each pipeline is running relative to its maximum — identifies bottlenecks
""")


render_key_concepts([
    {"term": "Cortex Analyst", "definition": "Snowflake's text-to-SQL engine. Converts natural language to SQL using a semantic view for context. Understands domain-specific terms like SOR, API gravity, and WCS discount when given proper AI instructions."},
    {"term": "Semantic View", "definition": "A first-class Snowflake object mapping tables to business concepts. Contains relationships, facts, dimensions, metrics, synonyms, and AI instructions."},
    {"term": "AI_SQL_GENERATION", "definition": "Custom instructions that guide SQL generation. Essential for energy domain — tells Analyst that 'SOR' means steam-oil ratio, 'SAGD' is a thermal extraction method, etc."},
])

render_what_you_built([
    "ENERGY_OPERATIONS_VIEW semantic view with 6 tables and domain-specific metrics",
    "Natural language queries for production, pipeline, and transport data",
    "Expanded view with calculated efficiency and compliance metrics",
])
