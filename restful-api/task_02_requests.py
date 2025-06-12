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
    filter_post = []
    for post in posts:
        filter_post.append({
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        })
        with open('posts.csv', 'w', newline='') as csvfile:
            write = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            write.writerheads()
            for post in posts:
                write.writerow({"id": post["id"],
                                "title": post["title"], "body": post["body"]})
    else:
        print("Failed to fetch posts. Status code: {}".format("response.status_code"))


fetch_and_print_posts()
fetch_and_save_posts()
