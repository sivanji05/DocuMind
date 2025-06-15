import tempfile
import boto3
import os
from app.core.config import settings
from app.services.es_service import index_document_chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
from elasticsearch import Elasticsearch
from unstructured.partition.auto import partition

from langchain_openai import OpenAIEmbeddings

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)

es = Elasticsearch(settings.ELASTICSEARCH_URL)

OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

embedding_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
def process_document(document_id: str, s3_path: str):
    """
    Download a document from S3, parse and chunk it, embed each chunk,
    and store results in Elasticsearch.
    """
    tmp_path = None
    try:
        # Step 1: Download from S3 to temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            s3.download_fileobj(settings.S3_BUCKET_NAME, s3_path, tmp)
            tmp_path = tmp.name

        # Step 2: Extract text using `unstructured`
        try:
            elements = partition(filename=tmp_path)
            full_text = "\n\n".join([str(el) for el in elements])
        except Exception as e:
            print("Parsing error:", e)
            return

        # Step 3: Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(full_text)

        if not chunks:
            print("No text chunks extracted from document.")
            return

        # Step 4: Generate embeddings
        try:
            embeddings = embedding_model.embed_documents(chunks)
        except Exception as e:
            print("Embedding error:", e)
            return

        if len(embeddings) != len(chunks):
            print("Mismatch between number of chunks and embeddings.")
            return

        # Step 5: Index in Elasticsearch
        for i, chunk in enumerate(chunks):
            es_doc = {
                "document_id": document_id,
                "chunk_id": i,
                "content": chunk,
                "embedding": embeddings[i],
            }
            try:
                index_document_chunks(es_doc)  # this saves to ES
            except Exception as e:
                print(f"Elasticsearch indexing error for chunk {i}:", e)

        print(f"[RAG] Document {document_id} processed and indexed.")

    except Exception as e:
        print("Unexpected error during document processing:", e)
    finally:
        # Step 6: Cleanup temp file
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception as e:
                print("Error removing temp file:", e) 