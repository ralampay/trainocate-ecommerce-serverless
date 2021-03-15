import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

class SaveCourse:
  def __init__(self, code=None, name=None, description=None, price=None, num_days=None, endpoint_url=None, table_name=None):
    self.code         = code
    self.name         = name
    self.description  = description
    self.price        = price
    self.num_days     = num_days
    self.endpoint_url = endpoint_url
    self.table_name   = table_name

  def execute(self):
    dynamodb  = boto3.resource('dynamodb', endpoint_url=self.endpoint_url)
    table     = dynamodb.Table(self.table_name)

    obj = {
      "name":         self.name,
      "code":         self.code,
      "description":  self.description,
      "price":        Decimal(self.price),
      "num_days":     self.num_days
    }

    try:
      print("Saving course to table %s..." % (self.table_name))

      response  = table.put_item(
                    Item=obj
                  )

      obj["price"] = float(obj["price"])
    except ClientError as e:
      print(e.response['Error']['Message'])
      print("Something went wrong!")
    else:
      print("Successfully saved course %s..." % (self.code))

      return obj

    return False
