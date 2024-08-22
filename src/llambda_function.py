import random

def lambda_handler(event, context):
    responses = ["yes", "no", "maybe"]
    return {
        'statusCode': 200,
        'body': random.choice(responses)
    }
