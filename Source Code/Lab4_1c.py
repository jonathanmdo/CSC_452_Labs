"""
Lab 4 Q1C: Start and stop an Amazon EC2 instance
"""
# Import the libraries 
import sys
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the ec2 server
ec2 = boto3.client('ec2')
# Whatever the user input is for the argument, it will be uppercase
action = sys.argv[1].upper()
# If the action variable is "ON"
if action == 'ON':
    # Do a dry run first to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-0b2084831117948c8'], DryRun = True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry Run succeeded, can run start_instances again without dryrun
    try:
        response = ec2.start_instances(InstanceIds=['i-0b2084831117948c8'], DryRun = False)
        print(response)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print(e)
else:
    # Do a dry run first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=['i-0b2084831117948c8'], DryRun = True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry Run succeeded, can run start_instances again without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-0b2084831117948c8'], DryRun = False)
        print(response)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print(e)
    