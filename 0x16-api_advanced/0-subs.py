#!/usr/bin/python3
""" How many subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit
    """
    headers = {'User-agent': 'My User Agent'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except BaseException:
        return 0
