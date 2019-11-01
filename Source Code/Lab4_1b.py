"""
Lab 4 Q1B: Start and stop detailed monitoring of an EC2 instance
"""
# Import boto3 libraries 
import sys
import boto3
# Set the ec2 variable to connect to the ec2 client
ec2 = boto3.client('ec2')
# If the user set the index argument to "ON", it will monitor the specific instance that it was set to. 
# Else, it would set the response to unmonitored the specific instance
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-0404c7f35d4789f09'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-0404c7f35d4789f09'])
# Once we got the response variable, it will print out the result
print (response)