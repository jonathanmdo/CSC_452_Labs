


# Import boto3 Library
import boto3
# Create an S3 client
s3 = boto3.client('s3')
# set the variable containing the file name and the bucket name
filename = 'README.md'
bucket_name = 'jmd070lab41abucket'
# This will upload the file to s3 storage with the filename using the bucket name
s3.upload_file(filename, bucket_name, filename)

