import requests
import os

# API keys and endpoint
subscription_key = os.getenv("BING_SUBSCRIPTION_KEY")
endpoint = "https://api.bing.microsoft.com/v7.0/search"
query = "Microsoft"

# Request parameters
params = {'q': query, 'mkt': 'en-US'}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    # Extract news descriptions and URLs
    news_descriptions = []
    news_urls = []
    
    if 'news' in data:
        for article in data['news']['value']:
            news_descriptions.append(article['description'])
            news_urls.append(article['url'])
    
    # Print the results
    print("News Descriptions:")
    print(news_descriptions)
    print("\nNews URLs:")
    print(news_urls)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)


#Sample response
'''
News Descriptions:
['This way, Qualcomm’s new chips can run more kinds of apps that don’t have native ARM64 versions and, until now, weren’t usable with emulation. It could even enable games that use AVX2, like Starfield and Helldivers 2,', "Microsoft wants you to use Bing so badly, it'll pay a user a million bucks who switches to the search engine as part of a huge sweepstakes.", 'Microsoft is adding AI-powered text editing to Notepad. The feature, called Rewrite, is rolling out in preview to Windows Insiders and will let you use AI to “rephrase sentences, adjust tone, and modify the length of your content,', 'Microsoft has started testing AI-powered Notepad text rewriting and Paint image generation tools four decades after the two programs were released in the 1980s.', 'Microsoft is reimaging the way Xbox Game Pass Quests award Rewards points, but only some players are currently able to try out these new changes.']

News URLs:
['https://www.msn.com/en-us/money/other/microsoft-s-new-emulator-could-bring-more-games-to-windows-on-arm/ar-AA1tDE07', 'https://www.msn.com/en-us/news/technology/desperate-microsoft-will-pay-1000000-to-someone-who-actually-uses-bing/ar-AA1tDu9i', 'https://www.msn.com/en-us/news/technology/soon-you-can-let-microsoft-s-notepad-rewrite-text-for-you/ar-AA1tCZyP', 'https://www.bleepingcomputer.com/news/microsoft/microsoft-notepad-to-get-ai-powered-rewriting-tool-on-windows-11/', 'https://gamerant.com/microsoft-new-xbox-game-pass-quests-australia-only/']
'''
