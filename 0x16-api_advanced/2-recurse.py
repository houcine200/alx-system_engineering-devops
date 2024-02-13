#!/usr/bin/python3
import requests
"""
Queries the Reddit API to get the titles
of all hot articles for a given subreddit.
"""


def recurse(subreddit, hot_list=[]):
    """return top ten post titles recursively"""
    after = ""
    url = 'https://www.reddit.com/r/{}/hot.json".format(subreddit)'
    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['data']['after']

    return recurse(subreddit, hot_list)
