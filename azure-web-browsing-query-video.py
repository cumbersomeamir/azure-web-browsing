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


'''
Sample Response

The video URLs are: ['https://www.youtube.com/watch?v=4k2T5sfGIP4', 'https://www.youtube.com/watch?v=ySKjhmg9RRo', 'https://www.youtube.com/watch?v=qaIbfivuqu0', 'https://www.youtube.com/watch?v=Ttmta1hTehU', 'https://www.youtube.com/watch?v=nKcyU8hh14Q', 'https://www.youtube.com/watch?v=FZhbJZEgKQ4', 'https://www.youtube.com/watch?v=XYUEQ0SyOyE', 'https://www.youtube.com/watch?v=Kxf3Az-3sCo', 'https://www.youtube.com/watch?v=VjRCApJBRIQ', 'https://www.youtube.com/watch?v=c9xCv2AwuyU', 'https://www.youtube.com/watch?v=eaiYQ8uzGsw', 'https://www.youtube.com/watch?v=1U9hL58QcII', 'https://www.youtube.com/watch?v=AgKt1FZyb04', 'https://www.youtube.com/watch?v=9FOQYQBPCeo', 'https://www.youtube.com/watch?v=M2oyfykzT5E', 'https://www.youtube.com/watch?v=FWQOXv-MrKM', 'https://www.youtube.com/watch?v=BYR_S6ktoFc', 'https://www.youtube.com/watch?v=R7Cmcy6a9L8', 'https://www.youtube.com/watch?v=kR-HN6LHHR4', 'https://www.youtube.com/watch?v=jvEJBW7lLps', 'https://www.youtube.com/watch?v=Y8CvgtPT4OM', 'https://www.youtube.com/watch?v=dJnj2d4m63A', 'https://www.youtube.com/watch?v=tKuF_eoA7rU', 'https://www.youtube.com/watch?v=uX3A0C-A-Xw', 'https://www.youtube.com/watch?v=oMu-E3knVHU', 'https://www.youtube.com/watch?v=y8J0kXJk97s', 'https://www.youtube.com/watch?v=P5VE6PVsqTE', 'https://www.youtube.com/watch?v=Vzwsek-EbYk', 'https://www.youtube.com/watch?v=JLDw9TXulVo', 'https://www.youtube.com/watch?v=iorRpN0p1mc', 'https://www.youtube.com/watch?v=YEfnbXlcU_M', 'https://www.youtube.com/watch?v=4Lel1OwqLus', 'https://www.youtube.com/watch?v=AOaMuCRI5nE', 'https://www.youtube.com/watch?v=BNLEiLeIHoQ', 'https://learn.microsoft.com/en-us/viva/engage/overview']
'''
