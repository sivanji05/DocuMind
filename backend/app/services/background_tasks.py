import tempfile
import boto3
import os
from app.core.config import settings
from app.services.es_service import index_document_chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
from uuid import UUID

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from app.services.embedding_service import embedding_model



s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)
 
embedding_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))


def process_uploaded_file(document_id: UUID, s3_key: str):
    """
    Background task to process uploaded document: extract text, chunk, embed, index.
    """
    print(f"[Background] Processing document {document_id} from {s3_key}")

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        s3.download_fileobj(settings.S3_BUCKET_NAME, s3_key, tmp_file)
        tmp_file_path = tmp_file.name
    try:
        loader = None
        if s3_key.endswith(".pdf"):
            loader = PyPDFLoader(tmp_file_path)
        elif s3_key.endswith(".docx"):
            loader = Docx2txtLoader(tmp_file_path)
        elif s3_key.endswith(".csv"):
            loader = TextLoader(tmp_file_path)
        elif s3_key.endswith(".txt"):
            loader = TextLoader(tmp_file_path)
        elif s3_key.endswith(".md"):
            loader = TextLoader(tmp_file_path)
        elif s3_key.endswith(".json"):
            loader = TextLoader(tmp_file_path)
        elif s3_key.endswith(".html"):
            loader = TextLoader(tmp_file_path)
        elif s3_key.endswith(".xml"):
            loader = TextLoader(tmp_file_path)
    except Exception as e:
        print("[Background] Unsupported file type:", s3_key)
        return

    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    print(f"[Background] Split into {len(chunks)} chunks")

    for idx, chunk in enumerate(chunks):
        vector = embedding_model.embed_query(chunk.page_content)
        doc = {
            "document_id": str(document_id),
            "chunk_id": idx,
            "content": chunk.page_content,
            "embedding": vector
        }
        index_document_chunks(doc)

    print(f"[Background] Indexed all chunks for document {document_id}")
