


# Import Libraries
import boto3
import logging
import json
# set the variables 
filename = 'README2.md'
bucket_name = 'jmd070lab41abucket'
key = 'README.md'
# Connect to the s3 storage
s3 = boto3.client('s3')
# Set the response variable to get the bucket access control list using the bucket name
response = s3.get_bucket_acl(Bucket = bucket_name)
# Print the response
print(response)
