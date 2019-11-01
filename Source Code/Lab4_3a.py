# Import Libraries
from __future__ import print_function
import boto3

# Connect to the dynamodb database
dynamodb = boto3.client('dynamodb')

# Set the response variable to create a table name "Movies" with different attributes such as year and title 
# The year and title are in a dictionary format to apply key values to it
response = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Print the response
print(response)
