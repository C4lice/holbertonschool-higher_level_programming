#!/usr/bin/python3

from typing import Dict
import requests
import csv

def fetch_and_print_posts():
    '''
    This function prints the reponded JSON from an HTTPS request to console.
    '''

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    '''
    This function writes the reponded JSON from an HTTPS request to a CSV file.
    '''

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        headers = ['id', 'title', 'body']

        filtered_posts = [
            {key: post[key] for key in headers}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(filtered_posts)
