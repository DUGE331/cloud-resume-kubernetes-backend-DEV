import boto3
import os
import json

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("VISITOR_TABLE", "CloudResumeVisitors-Dev")
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    method = event.get("httpMethod", "GET")

    if method == "GET":
        # Return visitor count
        response = table.get_item(Key={"id": 1})
        count = response.get("Item", {}).get("count", 0)
        return {
            "statusCode": 200,
            "body": json.dumps({"visitor_count": count})
        }

    elif method == "POST":
        # Increment visitor count
        table.update_item(
            Key={"id": 1},
            UpdateExpression="SET count = if_not_exists(count, :start) + :inc",
            ExpressionAttributeValues={":inc": 1, ":start": 0},
            ReturnValues="UPDATED_NEW"
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Visitor added!"})
        }

    else:
        # Unsupported method
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Unsupported method"})
        }