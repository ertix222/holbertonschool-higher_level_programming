#!/usr/bin/python3
"""script to fetch posts from a public API
and print or save them.
"""


import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        print("Status Code: 200")
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        print(posts[0])


fetch_and_print_posts()
fetch_and_save_posts()
