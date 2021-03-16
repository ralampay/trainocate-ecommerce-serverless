import json
import boto3
import os
from botocore.exceptions import ClientError
from xendit import Xendit
import uuid

from validate_payment_details import ValidatePaymentDetails

def lambda_handler(event, context):
  print(event)
  # Which dynamodb endpoint we will connect to
  endpoint_url  = os.environ.get("DYNAMODB_URL")
  table_name    = os.environ['TABLE_NAME_COURSES']
  api_key       = os.environ['XENDIT_API_KEY']

  params = json.loads(event["body"])
  print(params)

  first_name        = params.get("first_name")
  middle_name       = params.get("middle_name")
  last_name         = params.get("last_name")
  company           = params.get("company")
  email             = params.get("email")
  contact_number    = params.get("contact_number")
  course            = params.get("course")
  credit_card_token = params.get("credit_card_token")
  credit_card_cvn   = params.get("cvn")
  external_id       = uuid.uuid1()

  validator = ValidatePaymentDetails(
                first_name=first_name,
                last_name=last_name,
                email=email,
                contact_number=contact_number,
                course=course,
                credit_card_token=credit_card_token,
                credit_card_cvn=credit_card_cvn
              )

  validator.execute()

  if len(validator.errors) > 0:
    errors = validator.errors

    return {
      "statusCode": 403,
      "body": json.dumps({
        "message": "invalid transaction",
        "errors": errors
      }),
      "headers": {
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
      }
    }

  xendit_instance = Xendit(api_key=api_key)
  credit_card     = xendit_instance.CreditCard

  charge  = credit_card.create_charge(
              token_id=credit_card_token,
              external_id=external_id,
              amount=course.get('price'),
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
