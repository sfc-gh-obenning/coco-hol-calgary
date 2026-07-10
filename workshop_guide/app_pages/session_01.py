import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(1, "Data Prep", "9:15 - 9:30 AM", "15 min", "Database, schema, warehouse, and 9 operational tables loaded from CSV")

render_technologies_used([
    {"name": "Database & Schema", "description": "Snowflake's organizational hierarchy for objects. A database contains schemas, and schemas contain tables, views, and other objects.", "icon": "database"},
    {"name": "CSV File Format", "description": "Snowflake can infer schema and load data directly from CSV files using file formats and COPY INTO commands.", "icon": "table_chart"},
    {"name": "Virtual Warehouse", "description": "Snowflake's compute engine. A warehouse provides the CPU and memory to execute queries and load data. Scales independently of storage.", "icon": "memory"},
])


PROMPT_1_1 = """Create the following Snowflake objects for our Alberta Energy AI workshop:

1. A database called ENERGY_AI
2. A schema called OPS inside that database
3. A stage called DATA in the schema OPS with a directory table and server side encryption
3. A warehouse called ENERGY_WH (size MEDIUM, auto-suspend after 60 seconds, auto-resume enabled)
4. Set the session context to use these objects

Execute all SQL and confirm each object was created."""

render_prompt("Prompt 1.1", "Create Database, Schema & Warehouse", PROMPT_1_1)

render_explanation("What this prompt does", """
Creates the foundational Snowflake objects:

```sql
CREATE DATABASE ENERGY_AI;
CREATE SCHEMA ENERGY_AI.OPS;
CREATE WAREHOUSE ENERGY_WH
  WAREHOUSE_SIZE = 'MEDIUM'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE DATABASE ENERGY_AI;
USE SCHEMA OPS;
USE WAREHOUSE ENERGY_WH;
```
""")


PROMPT_1_2 = """In ENERGY_AI.OPS, the 9 CSV files have been uploaded to an internal stage called DATA.

For all 9 tables (FACILITIES, PIPELINES, PRODUCTION_RECORDS, TRANSPORT_INVOICES, PIPELINE_THROUGHPUT, WELL_MONITORING, SAFETY_INCIDENT_LOGS, ENVIRONMENTAL_REPORTS, AER_INSPECTION_REPORTS):

1. Create a file format (CSV with PARSE_HEADER=TRUE, FIELD_OPTIONALLY_ENCLOSED_BY='"')
2. Create the tables with appropriate column types inferred from the data. Ensure to convert the column names to uppercase.
3. Load the data

Use CREATE TABLE with INFER_SCHEMA from a stage and then COPY INTO them. The key requirement is that all 9 tables are created and populated.

Execute all SQL."""

st.markdown("""
**Before running the prompt below, download the 9 CSV files and upload them to the `DATA` stage:**

1. Download all files from [github.com/sfc-gh-obenning/coco-hol-calgary/tree/main/workshop_guide/data](https://github.com/sfc-gh-obenning/coco-hol-calgary/tree/main/workshop_guide/data):
   `facilities.csv`, `pipelines.csv`, `production_records.csv`, `transport_invoices.csv`, `pipeline_throughput.csv`, `well_monitoring.csv`, `safety_incident_logs.csv`, `environmental_reports.csv`, `aer_inspection_reports.csv`
2. Using Snowsight, use the Horizon Catalog to browse to the `ENERGY_AI.OPS.DATA` stage to upload all 9 files.
3. Then copy the prompt below into Cortex Code and execute.
""")

render_prompt("Prompt 1.2", "Load and Create Tables from CSV", PROMPT_1_2)

render_explanation("What this prompt does", """
Loads all 9 operational data tables from CSV files uploaded to the internal stage `DATA`:

```sql
CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = CSV
  PARSE_HEADER = TRUE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE TABLE FACILITIES
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    FROM TABLE(INFER_SCHEMA(
      LOCATION => '@ENERGY_AI.OPS.DATA/facilities.csv',
      FILE_FORMAT => 'csv_format'
    ))
  );

COPY INTO FACILITIES
  FROM @ENERGY_AI.OPS.DATA/facilities.csv
  FILE_FORMAT = csv_format;
```

**The 9 tables**:
| Table | Rows | Description |
|-------|------|-------------|
| FACILITIES | 5 | Oil sands and pipeline facilities |
| PIPELINES | 20 | Major crude and gas pipelines |
| PRODUCTION_RECORDS | 200 | Bitumen/crude production records |
| TRANSPORT_INVOICES | 300 | Crude transport and sales invoices |
| PIPELINE_THROUGHPUT | 400 | Hourly pipeline flow metrics |
| WELL_MONITORING | 300 | SAGD well performance data |
| SAFETY_INCIDENT_LOGS | 40 | Safety and environmental incidents |
| ENVIRONMENTAL_REPORTS | 20 | Environmental compliance reports |
| AER_INSPECTION_REPORTS | 25 | Alberta Energy Regulator inspections |
""")


PROMPT_1_3 = """Run a query in ENERGY_AI.OPS that shows every table name and its row count, ordered by row count descending. Format it nicely."""

render_prompt("Prompt 1.3", "Verify All Data Tables", PROMPT_1_3)

render_explanation("What this prompt does", """
A quick verification query. You should see approximately **1,510 total rows** across 9 tables.
""")


render_key_concepts([
    {"term": "Internal Stage", "definition": "A named Snowflake stage that stores files within Snowflake's managed storage. Files are uploaded via Snowsight UI or PUT command and can be used with COPY INTO and INFER_SCHEMA."},
    {"term": "INFER_SCHEMA", "definition": "A Snowflake table function that automatically detects column names and types from files in a stage. Eliminates manual CREATE TABLE DDL for well-structured CSV files."},
    {"term": "File Format", "definition": "A named object specifying how to parse files (CSV delimiters, headers, quoting). Created once and reused across multiple COPY INTO operations."},
])

render_what_you_built([
    "ENERGY_AI database and OPS schema",
    "ENERGY_WH warehouse (Medium, auto-suspend 60s)",
    "9 operational data tables loaded from CSV (~1,510 total rows)",
])
