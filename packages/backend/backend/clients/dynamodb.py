import boto3
from common.settings import DynamoDB

dynamodb = boto3.resource(
    service_name=DynamoDB.SERVICE_NAME,
    endpoint_url=DynamoDB.ENDPOINT_URL,
    aws_access_key_id=DynamoDB.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=DynamoDB.AWS_SECRET_ACCESS_KEY,
    region_name=DynamoDB.REGION_NAME,
)
