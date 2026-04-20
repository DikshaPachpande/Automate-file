import boto3
import os

# Debug: check files
print(" Files in current directory:")
print(os.listdir())

# Get environment variables
bucket_name = os.getenv("S3_BUCKET_NAME")
region = os.getenv("AWS_REGION")

if not bucket_name:
    raise Exception(" S3_BUCKET_NAME not set")

# Create S3 client (credentials auto from GitHub Actions)
s3 = boto3.client("s3", region_name=region)

try:
    print("⬆️ Uploading index.html...")
    
    s3.upload_file(
        "index.html",   # local file
        bucket_name,    # bucket
        "automated-file-upload-on-s3"    # S3 path (ROOT FIX)
    )

    print(" Upload successful!")

except Exception as e:
    print(" Upload failed:", e)
    raise
