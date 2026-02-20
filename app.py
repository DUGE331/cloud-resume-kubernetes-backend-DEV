import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['VISITOR_TABLE']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Use the correct partition key name and type
    key = {"visitor_count": 1}  # Number type, matches your table

    # Get current count safely
    response = table.get_item(Key=key)
    count = response.get('Item', {}).get('count', 0)

    # Increment count
    count += 1

    # Write back to table
    table.put_item(Item={"visitor_count": 1, "count": count})

    return {
        "statusCode": 200,
        "body": {"visitor_count": count}
    }