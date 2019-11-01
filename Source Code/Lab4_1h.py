"""
Lab 4 Q1H: Get information about your security groups 
"""
# Import the libraries 
import sys
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the ec2 server
ec2 = boto3.client('ec2')
# Try to set the response variable to get information about the security group. Print success and the response variable. 
# Else, it fails and prints out a error message.
try:
    response = ec2.describe_security_groups(GroupIds = ['sg-037063ee8ab916fce'])
    print("Success",response)
except ClientError as e:
    print(e)