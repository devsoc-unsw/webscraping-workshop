#!/usr/bin/env python3

# Example 1: Basic HTTP Requests
# Learn how to make HTTP requests to APIs and websites
# By Chris Casolin, November 2025
# Written for Devsoc Training Program's Intro to Web Scraping Workshop

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import re
import html
from helper import print_ex

################################################################################
def ex1_1():
    print_ex(1.1, "Basic API Request", topgap=False)

    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    # https://www.w3schools.com/python/ref_requests_response.asp

    print(f"Status Code: {response.status_code}")
    # https://www.w3schools.com/tags/ref_httpmessages.asp
    print(f"Content Type: {response.headers['Content-Type']}")
    print(f"Response Body:")

    # Parse JSON response
    data = response.json()
    print(f"\tTitle: {data['title']}")
    print(f"\tUser ID: {data['userId']}")
    print(f"\tBody Preview: {data['body'][:100]}...")

################################################################################
def ex1_2():
    print_ex(1.2, 'API Request with Parameters')
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        "userId": 2,
        "_limit": 3
    }

    response = requests.get(url, params=params)
    print(f"Request URL: {response.url}")
    print(f"Status Code: {response.status_code}")

    posts = response.json()
    print(f"\Received {len(posts)} posts:")
    for i, post in enumerate(posts, 1):
        print(f"\t{i}. {post['title']}")

################################################################################
def ex1_3():
    print_ex(1.3, 'Raw HTML Scraping - First Attempt')

    url = "http://httpbin.org/user-agent"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    print(f"Response shows our user-agent:")
    data = response.json()
    print(f"\tuser-agent: {data['user-agent']}")
    print()

    print("Trying a site that checks User-Agent:")
    try:
        response = requests.get("https://en.wikipedia.org/wiki/Web_scraping", timeout=5)
        print(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

################################################################################
def ex1_4():
    print_ex(1.4, 'Adding User-Agent Headers')

    headers_browserlike = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    headers_simple = {
        "User-Agent": "web scraping demo 1.0"
    }

    # Test with headers
    response = requests.get("http://httpbin.org/user-agent", headers=headers_simple)
    data = response.json()
    print(f"Now our user-agent is: '{data['user-agent']}'")
    print()

    # Try scraping with headers
    print(f"Scraping wikipedia with proper headers:")
    response = requests.get("https://en.wikipedia.org/wiki/Web_scraping", headers=headers_simple)
    print(f"Status Code: {response.status_code}")
    print(f"Content Type: {response.headers['Content-Type']}")
    print(f"Page size: {len(response.text)} characters")

################################################################################
def ex1_5():
    print_ex(1.5, 'Error Detection and Handling')
    print("Testing various error scenarios:")
    print()

    # 404 Not Found
    print("1. Testing 404 error:")
    try:
        response = requests.get("http://httpbin.org/status/404", timeout=5)
        # Raise exception if there is an error
        response.raise_for_status()
        print("\tPlease dont print --> should 404")
    except requests.exceptions.HTTPError as e:
        print(f"\tFailed successfully: {e}")
        print(f"\tStatus code: {response.status_code}")
    print()

    # Timeout
    print("2. Testing timeout:")
    try:
        # 5 second delay, 2 second timeout
        response = requests.get("http://httpbin.org/delay/5", timeout=2)
        print("\Please dont print --> should timeout first")
    except requests.exceptions.Timeout:
        print("\tSuccessfully caught request timeout")
    except requests.exceptions.RequestException as e:
        print(f"\tSomething else happened: {e}")
    print()
    
    # Connection error
    print("3. Testing connection error:")
    try:
        response = requests.get("http://fakeahhwebsite.com", timeout=3)
        print("\tPlease dont print --> url is fake")
    except requests.exceptions.ConnectionError:
        print("\tSuccessfully failed to connect")
    except requests.exceptions.RequestException as e:
        print(f"\tSomething else happened: {e}")

################################################################################
def ex1_6():
    print_ex(1.6, 'Parse HTML with Regex')
    
    response = requests.get("http://quotes.toscrape.com/")
    html_content = response.text
    
    # print(html_content[:120])
    
    title_pattern = re.compile(r"<title>(.*)</title>")
    title = title_pattern.search(html_content)
    print("Found Title:")
    print(f"\t{title.group(1)}")
    print()
    
    quote_pattern = re.compile(r'''<span class="text" itemprop="text">(.*)</span>''')
    quotes = quote_pattern.findall(html_content)
    print("Found Quotes:")
    for q in quotes:
        print(f"\t{html.unescape(q[1:-1])}")

################################################################################
# Run all examples
if __name__ == "__main__":
    ex1_1()
    ex1_2()
    ex1_3()
    ex1_4()
    ex1_5()
    ex1_6()