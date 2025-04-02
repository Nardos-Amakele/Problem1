 How to Run
Install dependencies:


pip install -r requirements.txt
Start server:


python app.py
Test endpoints:


# Ask question
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is SingularityNET?"}'

# Add new fact
curl -X POST http://localhost:8000/update \
-H "Content-Type: application/json" \
-d '{"fact":"(FAQ \\"New question\\" \\"New answer\\")"}'

🔍 Detailed Message Flow
User Query:

POST request to /ask with question text

Processing Pipeline:

app.py → process-query → generate-response → find-faq/get-tech-stack → LLM fallback

Knowledge Graph Lookup:

First tries exact FAQ match (find-faq)

If none, searches for related technologies (get-tech-stack)

Falls back to LLM if no knowledge graph results
Response:

Returns either:

Exact FAQ answer

Related technologies

LLM-generated response

Knowledge Updates:

New facts added via /update endpoint

Immediately available for future queries

Key Features Implemented
Knowledge Graph Integration:

Types, entities, and relationships in domain.metta

Real-time updates via API

Context-Aware Responses:

Rule-based inference in rules.metta

Multi-Source Answers:

Priority to KG facts

LLM fallback when needed

Adaptive Learning:

Dynamic knowledge updates

Growing FAQ database

