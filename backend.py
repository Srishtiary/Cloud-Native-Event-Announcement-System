import json
import boto3
import os

# Get config from environment variables
region = os.environ.get("AWS_REGION", "ap-south-1")
sns_client = boto3.client("sns", region_name=region)
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

def lambda_handler(event, context):
    try:
        if "body" in event and isinstance(event["body"], str):
            body = json.loads(event["body"])
        else:
            body = event
    except Exception as e:
        return {"statusCode": 400, "body": json.dumps({"error": f"Invalid request format: {str(e)}"})}

    action = body.get("action")
    if action == "subscribe":
        email = body.get("email")
        if not email:
            return {"statusCode": 400, "body": json.dumps({"error": "Email is required"})}
        
        response = sns_client.subscribe(
            TopicArn=SNS_TOPIC_ARN,
            Protocol="email",
            Endpoint=email
        )
        return {
            "statusCode": 200,
            "body": json.dumps({
                "status": "success",
                "message": f"Confirmation email sent to {email}",
                "subscription_arn": response["SubscriptionArn"]
            })
        }

    title = body.get("title", "No Title")
    description = body.get("description", "No Description")
    date = body.get("date", "No Date Provided")

    message = f"📢 Event: {title}\n📝 Description: {description}\n📅 Date: {date}"

    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=f"New Event: {title}"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "success",
            "message_id": response["MessageId"],
            "event": body
        })
    }
