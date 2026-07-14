from fastapi import FastAPI
from services.medical_rag_service import retrieve_context
from api.models import RetrieveRequest

app = FastAPI(
    title="Medical RAG API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "status": "running"
    }

@app.post("/retrieve")
def retrieve(request: RetrieveRequest):

    result = retrieve_context(
        question=request.question
    )

    return result