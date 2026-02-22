import boto3
import os

# Get region from environment variable, fallback to default
region = os.environ.get("AWS_REGION", "ap-southeast-2")

# Pass the region to boto3
dynamodb = boto3.resource("dynamodb", region_name=region)
table = dynamodb.Table(os.environ["VISITOR_TABLE"])

def increment_visitor():
    response = table.update_item(
        Key={"visitor_count": 1},
        UpdateExpression="SET #c = if_not_exists(#c, :start) + :inc",
        ExpressionAttributeNames={"#c": "count"},
        ExpressionAttributeValues={":inc": 1, ":start": 0},
        ReturnValues="UPDATED_NEW"
    )
    return int(response["Attributes"]["count"])

#to run cd docker docker run --env-file .env -p 8000:8000 visitor-counter