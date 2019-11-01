"""
Lab 4 Q1G: Delete an existing key pair
"""
# Import the library 
import sys
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the EC2 server 
ec2 = boto3.client('ec2')
# Set the variable to delete the specific key pair
response = ec2.delete_key_pair(KeyName = 'bmr023Lab41fKey')
# print out the success message, along with the response
print("Success",response)
