import os
import requests
from pprint import pprint

# API keys and endpoint
subscription_key = os.getenv("BING_SUBSCRIPTION_KEY")
endpoint = "https://api.bing.microsoft.com/v7.0/videos/search"

query = "Microsoft"

# Request parameters
params = {'q': query, 'mkt': 'en-US'}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    # Convert response to JSON
    response_json = response.json()
    pprint(response_json)  # Print to inspect structure

    # Extract video URLs from the response JSON
    videos = response_json.get('value', [])
    video_urls = [video.get('contentUrl') for video in videos if 'contentUrl' in video]

    # Print the extracted URLs
    print("The video URLs are:", video_urls)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
