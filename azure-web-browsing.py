import json
import requests
from pprint import pprint

# API keys and endpoint
subscription_key = os.getenv("BING_SUBSCRIPTION_KEY")
backup_key = os.getenv("BING_BACKUP_KEY")  # Optional backup key
endpoint = "https://api.bing.microsoft.com/v7.0/search"
subscription_id = os.getenv("BING_SUBSCRIPTION_ID")
location = "Global"

# Query term(s) to search for.
query = "Microsoft"

# Request parameters
mkt = 'en-US'
params = {'q': query, 'mkt': mkt}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print("Headers:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
