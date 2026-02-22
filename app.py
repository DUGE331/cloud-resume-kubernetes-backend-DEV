import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['VISITOR_TABLE'])

def lambda_handler(event, context):
    key = {"visitor_count": 1}
    response = table.get_item(Key=key)
    count = response.get('Item', {}).get('count', 0)

    count += 1
    table.put_item(Item={"visitor_count": 1, "count": count})

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "visitor_count": int(count)
        })
    }