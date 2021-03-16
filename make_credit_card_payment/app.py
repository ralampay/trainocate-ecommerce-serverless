import json
import boto3
import os
from botocore.exceptions import ClientError
from xendit import Xendit
import uuid

def lambda_handler(event, context):
  print(event)
  # Which dynamodb endpoint we will connect to
  endpoint_url  = os.environ.get("DYNAMODB_URL")
  table_name    = os.environ['TABLE_NAME_COURSES']
  api_key       = os.environ['XENDIT_API_KEY']

  params = json.loads(event["body"])
  print(params)

  first_name        = params["first_name"]
  middle_name       = params["middle_name"]
  last_name         = params["last_name"]
  company           = params["company"]
  email             = params["email"]
  contact_number    = params["contact_number"]
  course            = params["course"]
  credit_card_token = params["credit_card_token"]
  credit_card_cvn   = params["cvn"]
  external_id       = uuid.uuid1()

  xendit_instance = Xendit(api_key=api_key)

  charge  = CreditCard.create_charge(
              token_id=credit_card_token,
              external_id=external_id,
              amount=course.price,
              card_cvn=credit_card_cvn
            )

  print(charge)
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": "ok"
    }),
    "headers": {
      'Access-Control-Allow-Methods': '*',
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    }
  }
