"""
Lab 4 Q1F: Create a key pair to access an Amazon EC2 instance 
"""
# import the library
import sys
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the EC2 server 
ec2 = boto3.client('ec2')
# This variable creates a new key pair with the desired name
response = ec2.create_key_pair(KeyName = 'bmr023Lab41fKey')
# print out the success and the response
print("Success",response)
