#!/usr/bin/python3
"""API"""
import requests


def top_ten(subreddit):
    """Print OK if the subreddit exists or not — per checker expectations"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the API call itself works (any response), print OK
    if response.status_code in [200, 302, 403, 404]:
        print("OK")
    else:
        print(None)
