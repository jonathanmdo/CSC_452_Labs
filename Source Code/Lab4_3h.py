# Import Libraries
from __future__ import print_function
import boto3

 
# Connect to the dynamodb database 
dynamodb = boto3.resource('dynamodb')
# Set the variable to the movie table 
table = dynamodb.Table('Movies')

# delete the table 
response = table.delete()

# print the response 
print(response)