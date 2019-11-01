"""
Lab 4 Q1E: Get information about your key pairs
"""
# import the libraries
import sys
import boto3
from botocore.exceptions import ClientError
# set the variable to connect to the EC2 server
ec2 = boto3.client('ec2')
# Describe the EC2 Key Pair
response = ec2.describe_key_pairs()
# Print success with the response
print("Success",response)
