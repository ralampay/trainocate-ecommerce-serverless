import boto3

# Parameters
TABLE_NAME_COURSES = "courses"

# utility function to check if table_name exists
def table_exists(table_name, dynamodb=None):
  if not dynamodb:
    dynamodb  = boto3.client(
                  'dynamodb',
                  endpoint_url="http://localhost:8000"
                )

  existing_tables = dynamodb.list_tables()['TableNames']

  return table_name in existing_tables

# Create the table for courses
def create_courses_table(dynamodb=None):
  if not dynamodb:
    dynamodb  = boto3.resource(
                  'dynamodb',
                  endpoint_url="http://localhost:8000"
                )

  if table_exists(TABLE_NAME_COURSES):
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

if __name__ == '__main__':
  create_courses_table()
