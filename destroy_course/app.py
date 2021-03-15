import json
import boto3
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):

  # Which dynamodb endpoint we will connect to
  endpoint_url  = os.environ["DYNAMODB_URL"]
  table_name    = os.environ['TABLE_NAME_COURSES']

  # DynamoDB setup
  dynamodb  = boto3.resource('dynamodb', endpoint_url=endpoint_url)
  table     = dynamodb.Table(table_name)

  params = json.loads(event["body"])
  print(params)

  name = params["name"]
  code = params["code"]

  try:
    print("Deleting course %s..." % (code))
    
    response  = table.delete_item(
                  Key={
                    'name': name,
                    'code': code
                  }
                )

    return {
      "statusCode": 200,
      "body": json.dumps({
        "message": "Successfully deleted course",
      }),
      "headers": {
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
      }
    }
     
  except ClientError as e:
    print(e.response['Error']['Message'])
    print("Something went wrong!")
