import json

def lambda_handler(event, context):
    request_data = json.loads(event['body'])

    about_video = request_data['about_video']
    timestamps = request_data['timestamps']
    about_channel = request_data['about_channel']
    other_videos = request_data['other_videos']
    about_products = request_data['about_products']
    website_link = request_data['website_link']
    contact_links = request_data['contact_links']


    response_body = {
        "about_video": about_video,
        "timestamps": timestamps,
        "about_channel": about_channel,
        "other_videos": other_videos,
        "about_products": about_products,
        "website_link": website_link,
        "contact_links": contact_links
    }

    # Return the response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body)
    }
