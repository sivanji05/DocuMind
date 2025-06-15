
# import boto3
# from botocore.exceptions import NoCredentialsError, ClientError
# from app.core.config import settings

# s3 = boto3.client(
#     's3',
#     aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
# )

# def upload_file_to_s3(file_obj, s3_path):
#     try:
#         s3.upload_fileobj(file_obj, settings.S3_BUCKET_NAME, s3_path)
#     except (NoCredentialsError, ClientError) as e:
#         raise Exception(f"S3 upload error: {str(e)}")



import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from app.core.config import settings

s3 = boto3.client(
    's3',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)

def upload_file_to_s3(file_obj, s3_path):
    try:
        s3.upload_fileobj(file_obj, settings.S3_BUCKET_NAME, s3_path)
    except (NoCredentialsError, ClientError) as e:
        raise Exception(f"S3 upload error: {str(e)}")
 