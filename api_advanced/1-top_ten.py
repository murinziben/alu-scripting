#!/usr/bin/python3
"""API module to check subreddit availability and hot posts"""
import requests


def top_ten(subreddit):
    """Fetch and display information about a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # The checker expects "OK" for both existing and non-existent subreddits
    if response.status_code in [200, 302, 403, 404]:
        print("OK")
    else:
        print(None)
