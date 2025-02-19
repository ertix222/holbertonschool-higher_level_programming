#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
    """
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
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        post_data = list()
        for post in posts:
            post_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
            with open('post.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
                writer.writeheader()
                writer.writerows(post_data)


fetch_and_print_posts()
fetch_and_save_posts()
