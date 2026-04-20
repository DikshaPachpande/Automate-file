import boto3
import os
import mimetypes

# Read environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Validate env variables
if not all([AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, BUCKET_NAME]):
    raise Exception(" Missing AWS configuration in environment variables")

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file(file_path, bucket, object_name):
    """Upload a single file to S3"""
    try:
        content_type, _ = mimetypes.guess_type(file_path)
        extra_args = {}

        if content_type:
            extra_args["ContentType"] = content_type

        s3.upload_file(
            file_path,
            bucket,
            object_name,
            ExtraArgs=extra_args
        )

        print(f"Uploaded: {object_name}")

    except Exception as e:
        print(f"❌ Failed to upload {object_name}: {e}")


def upload_all_files():
    """Upload all files from current directory"""
    for root, dirs, files in os.walk("."):
        for file in files:
            # Skip unnecessary files/folders
            if ".git" in root or ".github" in root or "__pycache__" in root:
                continue

            file_path = os.path.join(root, file)

            # Remove './' from path to keep clean S3 structure
            s3_path = file_path.replace("./", "")

            upload_file(file_path, BUCKET_NAME, s3_path)


if __name__ == "__main__":
    print("Starting deployment to S3...")
    upload_all_files()
    print("Deployment completed!")
