from elasticsearch import Elasticsearch , exceptions
from elasticsearch.exceptions import ApiError
from langchain_openai import OpenAIEmbeddings
import os
from app.core.config import settings

es = Elasticsearch(settings.ELASTICSEARCH_URL)
INDEX_NAME = "document_index"





# def create_index_if_not_exists():
#     try:
#         if not es.indices.exists(index=INDEX_NAME):
#             print(f"Creating index: {INDEX_NAME}")
#             es.indices.create(index=INDEX_NAME, body={
#                 "settings": {
#         "number_of_shards": 1,
#         "number_of_replicas": 0
#           },
#                 "mappings": {
#                     "properties": {
#                         "document_id": {"type": "keyword"},
#                         "chunk_id": {"type": "integer"},
#                         "content": {"type": "text"},
#                         "embedding": {
#                             "type": "dense_vector",
#                             "dims": 1536,
#                             "index": True,
#                             "similarity": "cosine",
#                             "index_options": {
#                                 "type": "hnsw"
#                             }
#                         }
#                     }
#                 }
#             })
#     except exceptions.ApiError as e:
#         print(f"[Elasticsearch] Error creating index: {e}")



# def create_index_if_not_exists():
#     if not es.indices.exists(index=INDEX_NAME):
#         mapping = {
#             "mappings": {
#                 "properties": {
#                     "document_id": {"type": "keyword"},
#                     "chunk_id": {"type": "integer"},
#                     "content": {"type": "text"},
#                     "embedding": {"type": "dense_vector", "dims": 1536}  # adjust dims to match OpenAI model
#                 }
#             }
#         }
#         es.indices.create(index=INDEX_NAME, body=mapping)




def create_index_if_not_exists():
    mapping = {
        "mappings": {
            "properties": {
                "document_id": {"type": "keyword"},
                "chunk_id": {"type": "integer"},
                "content": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": 1536}
            }
        }
    }
    try:
        print("Checking index exists…")
        exists = es.indices.exists(index=INDEX_NAME)
        print("Exists returned:", exists)
        if not exists:
            print("Creating with mapping:", mapping)
            resp = es.indices.create(index=INDEX_NAME, body=mapping)
            print("Create response:", resp)
    except Exception as e:
        print("ERROR:", type(e), str(e))
        if hasattr(e, 'info'):
            print("Info:", e.info)
        if hasattr(e, 'body'):
            print("Body:", e.body)





def index_document_chunks(doc: dict):
    """
    Index a document chunk in Elasticsearch.
    """
    try:
        es.index(index=INDEX_NAME, body=doc)
    except exceptions.ElasticsearchException as e:
        print("[Elasticsearch] Indexing error:", e)


def semantic_search(query_vector: list, top_k: int = 5):
    """
    Perform a vector similarity search.
    """
    try:
        response = es.search(index=INDEX_NAME, body={
            "size": top_k,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        "params": {"query_vector": query_vector}
                    }
                }
            }
        })
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except ApiError as e:
        print(f"Elasticsearch error: {e}")
        return []
