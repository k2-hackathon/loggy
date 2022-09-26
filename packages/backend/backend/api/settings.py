from dotenv import load_dotenv
import os

load_dotenv()


class DynamoDB:
    SERVICE_NAME = os.getenv("DYNAMODB_SERVICE_NAME")
    ENDPOINT_URL = os.getenv("DYNAMODB_ENDPOINT_URL")
    AWS_ACCESS_KEY_ID = os.getenv("DYNAMODB_AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("DYNAMODB_AWS_SECRET_ACCESS_KEY")
    REGION_NAME = os.getenv("DYNAMODB_REGION_NAME")
