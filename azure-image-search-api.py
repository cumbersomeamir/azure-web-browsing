import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import os

# Replace 'your-subscription-key' with your actual Bing subscription key
subscription_key = os.getenv("BING_SUBSCRIPTION_KEY")
search_url = "https://api.bing.microsoft.com/v7.0/images/search"
search_term = "puppies"

# Set up headers and parameters
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term,
            "license": "public",
            "imageType": "photo",
            "count": 5,
            "aspect": 'Tall'}

# Make the API request
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

# Store image URLs in queried_images
queried_images = [img["contentUrl"] for img in search_results["value"]]

print("Queried images ", queried_images)

'''
https://learn.microsoft.com/en-us/bing/search-apis/bing-image-search/reference/query-parameters
'''
