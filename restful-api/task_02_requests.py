#!/usr/bin/python3
"""Module T2"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them to a CSV file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()

        with open('post.csv', mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for post in posts:
                writer.writerow({"id": post["id"], "title": post["title"],
                                "body": post["body"]})
    else:
        print("Failed to fetch posts. Status code: {}".format(response.status_code))


fetch_and_print_posts()
fetch_and_save_posts()
