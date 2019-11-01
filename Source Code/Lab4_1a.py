"""
Lab 4: First Python Boto3 activity
"""
# Import Boto3 Library
import boto3
# Set the variable to connect to the client, which is ec2
ec2 = boto3.client('ec2')
# Set the response to describe the instance in ec2
response = ec2.describe_instances()
# print the response variable; outputting the information of the instance
print(response)
