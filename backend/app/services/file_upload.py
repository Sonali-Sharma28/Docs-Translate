import boto3
from fastapi import UploadFile

s3_client = boto3.client('s3', aws_access_key_id="AWS_KEY", aws_secret_access_key="AWS_SECRET")

def upload_file_to_s3(file: UploadFile):
    s3_client.upload_fileobj(file.file, "your-bucket-name", file.filename)
    return f"https://s3.amazonaws.com/your-bucket-name/{file.filename}"
