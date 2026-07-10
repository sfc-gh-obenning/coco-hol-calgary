import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Search", "9:55 - 10:15 AM", "20 min", "Knowledge base, Cortex Search service, and RAG query pattern")

render_technologies_used([
    {"name": "Cortex Search Service", "description": "A managed hybrid search engine combining vector (semantic) and keyword search with automatic reranking. Created with a single SQL statement.", "icon": "search"},
    {"name": "RAG (Retrieval Augmented Generation)", "description": "A pattern that retrieves relevant documents first, then passes them as context to an LLM for grounded answer generation.", "icon": "hub"},
    {"name": "SEARCH_PREVIEW", "description": "SQL function to query a Cortex Search Service. Supports text queries, column selection, filtering, and result limits.", "icon": "preview"},
])


PROMPT_3_1 = """In ENERGY_AI.OPS:

1. First, create a unified text table for search called ENERGY_KNOWLEDGE_BASE that combines:
   - SAFETY_INCIDENT_LOGS: incident_id as doc_id, 'safety_incident' as doc_type, description_text || ' Resolution: ' || resolution_text as content, category as metadata_category, severity as metadata_priority, incident_date as doc_date
   - ENVIRONMENTAL_REPORTS: report_id as doc_id, 'environmental_report' as doc_type, report_text || ' Recommended: ' || recommended_actions as content, report_type as metadata_category, status as metadata_priority, report_date as doc_date
   - AER_INSPECTION_REPORTS: report_id as doc_id, 'aer_inspection' as doc_type, findings_text as content, inspection_type as metadata_category, outcome as metadata_priority, inspection_date as doc_date

2. Then create a Cortex Search Service:
   CREATE OR REPLACE CORTEX SEARCH SERVICE energy_knowledge_search
     ON content
     ATTRIBUTES metadata_category, metadata_priority, doc_type
     WAREHOUSE = ENERGY_WH
     TARGET_LAG = '1 hour'
     EMBEDDING_MODEL = 'snowflake-arctic-embed-l-v2.0'
     AS (
       SELECT doc_id, doc_type, content, metadata_category, metadata_priority, doc_date
       FROM ENERGY_KNOWLEDGE_BASE
     );

Execute all SQL. Then verify with SHOW CORTEX SEARCH SERVICES."""

render_prompt("Prompt 3.1", "Create Cortex Search Service", PROMPT_3_1)

render_explanation("What this prompt does", """
Builds a unified knowledge base from 3 unstructured text sources (85 documents total) and creates a hybrid search service over them.

The search service automatically:
1. **Embeds** every document using `snowflake-arctic-embed-l-v2.0`
2. **Indexes** for both vector (semantic) and keyword (lexical) search
3. **Auto-refreshes** when source data changes
""")


PROMPT_3_2 = """In ENERGY_AI.OPS, query our energy_knowledge_search service using SEARCH_PREVIEW:

1. Search: "pipeline leak spill containment" - show top 3 results
2. Search: "H2S gas release safety" - show top 3 results
3. Search: "tailings pond environmental compliance" filtered to doc_type = 'environmental_report' - show top 3 results
4. Search: "AER directive non-compliance" - show top 3 results

Execute all 4 searches and show results."""

render_prompt("Prompt 3.2", "Query the Search Service", PROMPT_3_2)

render_explanation("What this prompt does", """
Tests different search capabilities across energy operations documents:

1. **"pipeline leak spill"** — Should find pipeline integrity incidents even when described as "release" or "seepage"
2. **"H2S gas release"** — Tests safety-specific terminology matching
3. **"tailings pond" with filter** — Tests attribute filtering to only environmental reports
4. **"AER directive non-compliance"** — Tests regulatory terminology across all document types
""")


PROMPT_3_3 = """In ENERGY_AI.OPS, implement a RAG pattern:

1. Question: "What are the most common safety incidents at Alberta energy facilities and what preventive measures have been effective?"

2. Retrieve top 5 documents from energy_knowledge_search, then pass to SNOWFLAKE.CORTEX.COMPLETE() with instructions to answer ONLY from the provided documents, cite doc_ids, and structure the answer with: 1) Common incident types, 2) Root causes, 3) Effective measures, 4) Recommendations.

Use claude-sonnet-4-6 as the model. Execute and show the RAG response."""

render_prompt("Prompt 3.3", "RAG Pattern: Search + Generate", PROMPT_3_3)

render_explanation("What this prompt does", """
Implements the full **RAG** pattern: retrieve relevant safety documents, then generate a grounded answer with citations.

This is the standard enterprise AI pattern — the LLM answers from YOUR data, not its training set, reducing hallucination and ensuring traceability.
""")


render_key_concepts([
    {"term": "Cortex Search Service", "definition": "A managed hybrid search engine created with SQL. Handles embedding, indexing, reranking, and auto-refresh automatically."},
    {"term": "RAG", "definition": "Retrieval Augmented Generation: retrieve documents, include as context in LLM prompt, generate grounded answer. The standard pattern for enterprise AI."},
    {"term": "Hybrid Search", "definition": "Combining vector search (semantic similarity) with keyword search (exact matching). Catches both synonyms and specific technical terms."},
])

render_what_you_built([
    "ENERGY_KNOWLEDGE_BASE — unified document table from 3 sources (85 documents)",
    "energy_knowledge_search — Cortex Search service with hybrid search",
    "4 search queries across safety, environmental, and regulatory documents",
    "Full RAG pipeline for grounded Q&A over energy operations data",
])
