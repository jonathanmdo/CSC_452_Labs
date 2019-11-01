# Import Libraries
from __future__ import print_function
import boto3
from boto3.dynamodb.conditions import Key, Attr
 
# Connect to the dynamodb database 
dynamodb = boto3.resource('dynamodb')
# Set the variables 
table = dynamodb.Table('Movies')
#print out a statement 
print("Movies from 2016")
# query to retrieve information about the specified input 
response = table.query(
   KeyConditionExpression=Key('year').eq(2016)
)

# Print the response
for i in response['Items']:
    print(i['year'], ":", i['title'])
