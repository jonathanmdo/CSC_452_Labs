"""
Lab 4 Q1I: Create a security group to access an Amazon EC2 instance 
"""
# Import The libraries 
import sys
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the ec2 server
ec2 = boto3.client('ec2')
# Try to create a new security group with the desired name and a description. 
# print success when it is done along with the responses. 
# If it fails, then it prints out the error.
try:
    response = ec2.create_security_group(GroupName = 'Lab41I', Description = 'Lab41I created 2019-10-17T14:51:45.873-05:00')
    print("Success",response)
except ClientError as e:
    print(e)