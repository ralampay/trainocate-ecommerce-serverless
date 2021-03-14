# trainocate-ecommerce-serverless

Serverless components for trainocate-ecommerce

## Requirements

* `aws-sam-cli` for local development
* `boto3`

## Setting Up DynamoDB for Local Development

1. Make sure to download and setup a local copy of DynamoDB from [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) and run it. By default, it will run in `http://localhost:8000`

2. Create the tables

```
python bin/init_tables.py
```
