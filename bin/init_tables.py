import boto3
import argparse

# Parameters
DYNAMODB_URL        = "http://172.17.0.1:8000"
TABLE_NAME_COURSES  = "courses"

# utility function to check if table_name exists
def table_exists(table_name, dynamodb_url):
  dynamodb  = boto3.client(
                'dynamodb',
                endpoint_url=dynamodb_url
              )

  existing_tables = dynamodb.list_tables()['TableNames']

  return table_name in existing_tables

# Create the table for courses
def create_courses_table(dynamodb_url):
  dynamodb  = boto3.resource(
                'dynamodb',
                endpoint_url=dynamodb_url
              )

  if table_exists(TABLE_NAME_COURSES, dynamodb_url):
    print("Table %s already exists! Dropping first..." % (TABLE_NAME_COURSES))
    dynamodb.Table(TABLE_NAME_COURSES).delete()

  print("Creating table %s..." % (TABLE_NAME_COURSES))

  table = dynamodb.create_table(
            TableName=TABLE_NAME_COURSES,
            KeySchema=[
              {
                'AttributeName': 'name',
                'KeyType':'HASH'
              },
              {
                'AttributeName': 'code',
                'KeyType':'RANGE'
              }
            ],
            AttributeDefinitions=[
              {
                'AttributeName': 'name',
                'AttributeType': 'S'
              },
              {
                'AttributeName': 'code',
                'AttributeType': 'S'
              }
            ],
            ProvisionedThroughput={
              'ReadCapacityUnits': 5,
              'WriteCapacityUnits': 5
            }
          )

def main():
  parser = argparse.ArgumentParser(description="Dynamodb loader Trainocate Ecommerce Serverless")
  parser.add_argument("--dynamodb-url", help="DynamoDB URL", type=str, default=DYNAMODB_URL)

  args = parser.parse_args()

  dynamodb_url  = args.dynamodb_url

  create_courses_table(dynamodb_url)

if __name__ == '__main__':
  main()
