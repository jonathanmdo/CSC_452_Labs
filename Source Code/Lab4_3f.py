# Import Libraries
from __future__ import print_function
import boto3
 

# Connect to the dynamodb database 
dynamodb = boto3.client('dynamodb')

# Set the variables 
title = 'Distributed Computing is Fun!'
year = 2016

# The batch write operation puts and deletes multiple items in one or more tables
response = dynamodb.batch_write_item(
    
    RequestItems={
        'Movies':[
            {
                "PutRequest":{
                    "Item":{
                        'year':{"N": str(year)},
                        'title':{"S": title}
                        
                    }
                }
            }
            ]
    }
    
)


# Print the response
print(response)
