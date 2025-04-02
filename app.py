# from fastapi import FastAPI
# from hyperon import MeTTa
# import json

# app = FastAPI()
# metta = MeTTa()

# # Load knowledge
# metta.run('''
#   !(import! &self knowledge/tech_domain.metta)
#   !(import! &self knowledge/rules.metta)
# ''')

# @app.post("/ask")
# async def ask(question: str):
#     # Query MeTTa
#     response = metta.run(f'''
#       !((py-atom motto.faq_agent) 
#         (user "{question}"))
#     ''')
#     return {"answer": str(response[0][0])}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
from hyperon import MeTTa
from pydantic import BaseModel
import json

app = FastAPI()
metta = MeTTa()

# Load knowledge
metta.run('''
  !(import! &self "knowledge/domain.metta")
  !(import! &self "knowledge/rules.metta")
  !(import! &self "agents/query_engine.metta")
''')

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Escape quotes for MeTTa
        safe_question = request.question.replace('"', '\\"')
        
        # Execute query
        response = metta.run(f'''
          !(process-query "{safe_question}")
        ''')
        
        return {
            "answer": str(response[0][0]),
            "source": "knowledge-graph" if "I don't know" not in str(response[0][0]) else "llm"
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/update")
async def update_knowledge(fact: str):
    metta.run(f'(add-atom &self {fact})')
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)