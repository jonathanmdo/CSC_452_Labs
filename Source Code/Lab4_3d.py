# Import Libraries
from __future__ import print_function
import boto3
 

# Connect to the dynamodb database
dynamodb = boto3.client('dynamodb')

# Set the variables
title = 'The Big New Movie: JMD070'
year = 2015

# Update the item in the table 
response = dynamodb.update_item(
    TableName = 'Movies',
    Key={
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
