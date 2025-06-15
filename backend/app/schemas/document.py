from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class DocumentCreateResponse(BaseModel):
    id: UUID
    file_name: str
    status: str
    created_at: datetime


class AskRequest(BaseModel):
    question: str
    document_id: str 