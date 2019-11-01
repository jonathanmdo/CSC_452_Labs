


# Import boto3 Library
import boto3
# set the s3 client variable to connect to s3 using boto3
s3_client = boto3.client('s3')
# set the response variable to list the buckets
response = s3_client.list_buckets()
# output the bucket names
print('Existing Buckets:')
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')