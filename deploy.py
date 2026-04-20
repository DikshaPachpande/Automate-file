
import boto3
import os

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv("automated-file-upload-on-s3")

file_name = "index.html"

try:
    s3.upload_file(
        file_name,
        bucket_name,
        file_name,
        ExtraArgs={'ContentType': 'text/html'}
    )
    print("✅ File uploaded successfully")

except Exception as e:
    print("❌ Upload failed:", e)
