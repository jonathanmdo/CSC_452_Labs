


# import libraries 
import logging
import boto3
from botocore.exceptions import ClientError

# This is a function with two input
def create_bucket(bucket_name, region=None):
    try:
        # if the region is none, connect to the s3 server create a bucket with the bucket name
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        # s3 client connects to s3 with the specified region. 
        # Prints out the location constraint with the region
        # Create a bucket with the desired bucket name with the configuration of the location   
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    # If that fails, it prints out an error message
    except ClientError as e:
        logging.error(e)
        return False
    # Line 29: if it doesn’t print out a message, it returns true.
    return True
# This calls the function
create_bucket('jmd070lab41abucket', 'us-east-2')