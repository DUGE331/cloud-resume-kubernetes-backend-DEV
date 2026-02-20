import boto3
import os
import json  # needed for json.dumps

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['VISITOR_TABLE'])

def lambda_handler(event, context):
    key = {"visitor_count": 1}  # DynamoDB key is a number
    response = table.get_item(Key=key)
    count = response.get('Item', {}).get('count', 0)

    count += 1
    table.put_item(Item={"visitor_count": 1, "count": count})

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"visitor_count": count})  # <- string for API Gateway
    }