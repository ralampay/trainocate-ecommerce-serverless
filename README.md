# trainocate-ecommerce-serverless

Serverless components for trainocate-ecommerce

## Requirements

* docker
* `aws-sam-cli` for local development
* `boto3`

## Setting Up DynamoDB for Local Development

1. Run a local copy of dynamodb via docker:

```
docker run -p 8000:8000 amazon/dynamodb-local
```

2. Create the tables

```
python bin/init_tables.py
```

To override the URL for dynamodb, pass `--dynamodb-url`:

```
python bin/init_tables.py --dynamodb-url http://localhost:8001
```

3. Run the local server endpoints

```
docker run -p 8000:8000 amazon/dynamodb-local
sam build && sam local start-api
```
