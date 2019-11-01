"""
Lab 4 Q1J: Create a new security group
"""
# Import the libraries 
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the ec2 server
ec2 = boto3.client('ec2')
# Try to delete the security group with the specific Group ID. 
# Print out the success and the response when its finished. 
# Else if it fails, it prints out the error message.
try:
    response = ec2.delete_security_group(GroupId='sg-070f208cd37256da0')
    print('Success',response)
except ClientError as e:
    print(e)