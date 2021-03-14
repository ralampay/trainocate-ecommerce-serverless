import json
import boto3
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):

  # Which dynamodb endpoint we will connect to
  endpoint_url  = "http://172.17.0.1:8000"
  table_name    = os.environ['TABLE_NAME_COURSES']

  # DynamoDB setup
  dynamodb  = boto3.resource('dynamodb', endpoint_url=endpoint_url)
  table     = dynamodb.Table(table_name)

  try:
    print("Fetching data from table %s..." % (table_name))
    response  = table.scan()

    return {
      "statusCode": 200,
      "body": json.dumps({
        "courses": response["Items"]
      })
    }
     
  except ClientError as e:
    print(e.response['Error']['Message'])
    print("Something went wrong!")
