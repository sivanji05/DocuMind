# import os
# from langchain_openai import OpenAIEmbeddings

# embedding_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))


from langchain_openai import OpenAIEmbeddings
import os

embedding_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))