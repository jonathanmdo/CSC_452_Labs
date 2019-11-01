# Import Libraries
from __future__ import print_function
import boto3
 

# Connect to the dynamodb database
dynamodb = boto3.client('dynamodb')

# Set the variables 
title = 'The Big New Movie'
year = 2015

# Get the specified attribute from the table 
response = dynamodb.get_item(
    TableName = 'Movies',
    Key={
        'year': {
            'N' : str(year)
            },
        'title': {
            'S' : title
            }
        },
    AttributesToGet=[
        'title',
        ]
    
)

# Print the response
print(response)
