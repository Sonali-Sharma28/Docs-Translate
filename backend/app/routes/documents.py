from fastapi import APIRouter, HTTPException
from services.nlp_agent import query_rag_agent, create_index, load_documents

router = APIRouter()

# Load documents and create index at startup
docs = load_documents("./documents")
index = create_index(docs)

@router.post("/query")
def ask_question(question: str):
    try:
        response = query_rag_agent(question, index)
        return {"question": question, "answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
