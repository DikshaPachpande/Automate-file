deploy.py:

import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'automated-file-upload-on-s3', 'index.html')
