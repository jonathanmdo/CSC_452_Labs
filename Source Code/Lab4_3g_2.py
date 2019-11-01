# Import Libraries
from __future__ import print_function
import boto3
from boto3.dynamodb.conditions import Key, Attr
 
# Connect to the dynamodb database 
dynamodb = boto3.resource('dynamodb')
# Set the variable 
table = dynamodb.Table('Movies')
# print out a statement 
print("Movies from 2016")
# Scan the table to look for a certain input 
response = table.scan(
   FilterExpression = Attr('year').eq(2016)
)

# Print the response
items = response['Items']
print(items)