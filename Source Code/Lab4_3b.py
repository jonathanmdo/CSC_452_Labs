# Import Libraries
from __future__ import print_function
import boto3
 

# Connect to the dynamodb database
dynamodb = boto3.client('dynamodb')

# set the variables 
title = 'The Big New Movie'
year = 2015
# set the key with values in the table 
response = dynamodb.put_item(
    TableName = 'Movies',
    Item={
        'year': {
            'N' : str(year)
            },
        'title': {
            'S' : title
            }
        }
    
)

# Print the response
print(response)
