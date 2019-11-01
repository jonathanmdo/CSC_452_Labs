


# Import Libraries 
import logging
import boto3
from botocore.exceptions import ClientError

# This is the function with 3 arguments including the bucket name, object name, and the expiration.
def create_presigned_url(bucket_name, object_name, expiration=3600):
    #Set the s3_client variable to connect to the s3 storage client
    s3_client = boto3.client('s3')
    try:
        #Try to set the response to the generated preassigned URL
        response = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name,'Key': object_name},ExpiresIn=expiration)
    #if it fails, then it will print an error
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    print(response)
    
# This will call the function with the desired arguments
create_presigned_url('lab41abucket', 'README.md', expiration=3600)
