from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from app.db import database, models
from app.services.s3_service import upload_file_to_s3
from app.schemas.document import DocumentCreateResponse, AskRequest
from app.services.background_tasks import process_uploaded_file
import uuid
from io import BytesIO
from typing import List
from app.services.embedding_service import embedding_model
# from app.services.auth_service import get_current_user
from app.services.es_service import semantic_search

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

 
@router.get("/documents/list", response_model=List[DocumentCreateResponse])
def list_documents(db: Session = Depends(get_db)):
    docs = db.query(models.Document).all()
    return [
        DocumentCreateResponse(
            id=doc.id,
            file_name=doc.file_name,
            status=doc.status,
            created_at=doc.created_at
        ) for doc in docs
    ]

@router.post("/upload", response_model=DocumentCreateResponse)
async def upload_document(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks,
    db: Session = Depends(get_db)
):
    if not file.filename.endswith((".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx", ".md", ".json", ".xml",".html")):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    file_id = str(uuid.uuid4())
    s3_path = f"documents/{file_id}_{file.filename}"

    # Read file content first (before S3 and DB ops)
    file_content = await file.read()

    # Upload to S3
    try:
        #upload_file_to_s3(file_content, s3_path)
        upload_file_to_s3(BytesIO(file_content), s3_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

    # Save to DB
    new_doc = models.Document(
        file_name=file.filename,
        s3_path=s3_path,
        file_size_kb=len(file_content), 
        status="UPLOADED"
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    # Trigger background processing
    background_tasks.add_task(process_uploaded_file, new_doc.id, s3_path)

    return DocumentCreateResponse(
        id=new_doc.id,
        file_name=new_doc.file_name,
        status="PROCESSING",
        created_at=new_doc.created_at
    )





# @router.post("/api/documents/ask")
# async def ask_question(req: AskRequest):
#     # Step 1: Embed the question
#     try:
#         question_embedding = embedding_model.embed_query(req.question)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Embedding failed: {e}")

#     # Step 2: Perform semantic search
#     try:
#         results = semantic_search(question=req.question, document_id=req.document_id)
#         # Filter results for the selected document_id
#         filtered = [res for res in results if res.get("document_id") == req.document_id]
#         if not filtered:
#             return {"answer": "No relevant chunks found for this document."}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Search failed: {e}")
    

    

#     # Step 3: Return top content as "answer" (simplest form)
#     answer = "\n\n".join([chunk["content"] for chunk in filtered])
#     return {"answer": answer}

@router.post("/api/documents/ask")
async def ask_question(req: AskRequest):
    try:
        question_embedding = embedding_model.embed_query(req.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding failed: {e}")

    try:
        results = semantic_search(question=req.question, document_id=req.document_id)
        filtered = [res for res in results if res.get("document_id") == req.document_id]
        if not filtered:
            return {"answer": "No relevant chunks found for this document."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")

    answer = "\n\n".join([chunk["content"] for chunk in filtered])
    return {"answer": answer}
