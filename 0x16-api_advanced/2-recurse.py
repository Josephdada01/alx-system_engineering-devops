#!/usr/bin/python3
"""a recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of
    all hot articles for a given
    subreddit. If no results are found for the
    given subreddit, the function should return None.
    """
    if not subreddit:
        return None
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except BaseException:
        return None
