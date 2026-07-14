from pydantic import BaseModel


class RetrieveRequest(BaseModel):
    question: str