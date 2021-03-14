import json

def lambda_handler(event, context):
  return {
      "statusCode": 200,
      "body": json.dumps({
      "message": "show course",
      # "location": ip.text.replace("\n", "")
    }),
  }
