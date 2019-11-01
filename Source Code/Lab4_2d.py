


# Import boto3 Library
import boto3
import botocore
# Create an S3 client
s3 = boto3.resource('s3')
# Set the variable including the filename, the key, and the bucket name
filename = 'README2.md'
bucket_name = 'jmd070lab41abucket'
key = 'README.md'
#Connect to the bucket name and download the files
s3.Bucket(bucket_name).download_file(key, filename)

