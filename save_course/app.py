import json
import boto3
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
  return {
      "statusCode": 200,
      "body": json.dumps({
      "message": "create course",
      # "location": ip.text.replace("\n", "")
    }),
  }
