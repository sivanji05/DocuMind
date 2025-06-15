# from pydantic_settings import BaseSettings

# import os
# from dotenv import load_dotenv

# class Settings(BaseSettings):
#     DATABASE_URL: str
#     SECRET_KEY: str
#     AWS_ACCESS_KEY_ID: str
#     AWS_SECRET_ACCESS_KEY: str
#     S3_BUCKET_NAME: str
#     AWS_REGION: str = "us-east-1"
#     ELASTICSEARCH_URL: str
#     OPENAI_API_KEY: str
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

#     class Config:
#         env_file = ".env"

# settings = Settings()



from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv() 


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    S3_BUCKET_NAME: str
    AWS_REGION: str = "us-east-1"
    ELASTICSEARCH_URL: str
    OPENAI_API_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
     

settings = Settings()