import json
import boto3
import os
from botocore.exceptions import ClientError
from validate_course import ValidateCourse
from save_course import SaveCourse

def lambda_handler(event, context):
  print(event)
  # Which dynamodb endpoint we will connect to
  endpoint_url  = os.environ["DYNAMODB_URL"]
  table_name    = os.environ['TABLE_NAME_COURSES']

  params = json.loads(event["body"])
  print(params)

  code        = params["code"]
  name        = params["name"]
  description = params["description"]
  price       = params["price"]
  num_days    = params["num_days"]

  validation  = ValidateCourse(
                  code=code,
                  name=name,
                  description=description,
                  price=price,
                  num_days=num_days
                )

  errors = validation.execute()

  if len(errors) > 0:
    return {
      "statusCode": 400,
      "body": json.dumps({
        "errors": errors
      }),
      "headers": {
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
      }
    }

  # Convert to proper data type
  price     = float(price)
  num_days  = int(num_days)

  obj = SaveCourse(
          code=code,
          name=name,
          description=description,
          price=price,
          num_days=num_days,
          endpoint_url=endpoint_url,
          table_name=table_name
        ).execute()

  if(type(obj) == bool):
    return {
      "statusCode": 400,
      "body": json.dumps({
        "message": "Something went wrong",
      }),
      "headers": {
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
      }
    }
  else:
    return {
      "statusCode": 200,
      "body": json.dumps({
        "course": obj,
      }),
      "headers": {
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
      }
    }
