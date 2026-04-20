import boto3
import os

print("Current files:", os.listdir())

bucket = os.environ.get("S3_BUCKET_NAME")

if not bucket:
    raise Exception("Bucket name missing")

s3 = boto3.client("s3")

print("Uploading index.html...")

s3.upload_file("index.html", bucket, "index.html")

print("✅ Upload complete")
