"""
Lab 4 Q1D: Reboot an Amazon EC2 instance
"""
# import the libraries
import sys
import boto3
from botocore.exceptions import ClientError
# Set the variable to connect to the ec2 server
ec2 = boto3.client('ec2')


# Do a dry run first to verify permissions
try:
    ec2.reboot_instances(InstanceIds=['i-0b2084831117948c8'], DryRun = True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("Do not have permission to reboot instance")
        raise
# Dry Run succeeded, can run start_instances again without dryrun
try:
    response = ec2.reboot_instances(InstanceIds=['i-0b2084831117948c8'], DryRun = False)
    print("Success",response)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print(e)
