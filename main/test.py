import boto3
import json

# Create a Boto3 Lambda client with the specified region
lambda_client = boto3.client('lambda', region_name='us-east-1')

# Define the event data
event_data = {
    "body": json.dumps({
        "about_video": "Sample video description",
        "timestamps": "0:00, 2:30, 5:45",
        "about_channel": "Sample channel description",
        "other_videos": "Link to other videos",
        "about_products": "Description of products",
        "website_link": "https://example.com",
        "contact_links": "Social media links"
    })
}

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName='your-lambda-function-name',
    InvocationType='RequestResponse',
    Payload=json.dumps(event_data)
)

# Parse the response
response_body = json.loads(response['Payload'].read())

# Print the response body
print(response_body)
