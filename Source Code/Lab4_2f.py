


# Import boto3 Library
import boto3
import logging
import json
# Set the s3 variable to connect to the s3 storage
s3 = boto3.client('s3')
# Set the bucket name with the specified bucket, filename, and key
filename = 'README2.md'
bucket_name = 'jmd070lab41abucket'
key = 'README.md'
# This will set the bucket policy
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect':'Allow',
        'Principal':'*',
        'Action':['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
    }]
}
# set the bucket policy variable, this will convert the bucket policy to JSON format since it is python
bucket_policy = json.dumps(bucket_policy)
# This will replace the policy fora specific Amazon S3 bucket. A bucket policy can be set.
s3.put_bucket_policy(Bucket = bucket_name, Policy = bucket_policy)

# The response variable is set to retrieve a bucket's policy by calling the AWS SDK
response = s3.get_bucket_policy(Bucket = bucket_name)
# This will print the response and the policy
print(response['Policy'])
