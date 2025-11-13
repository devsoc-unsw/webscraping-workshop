#!/usr/bin/env python3

# Example 2: HTML Parsing with BeautifulSoup
# See why we need proper HTML parsing instead of regex
# By Chris Casolin, November 2025
# Written for Devsoc Training Program's Intro to Web Scraping Workshop

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup, Tag
import html
from helper import print_ex

################################################################################
def ex2_1():
    print_ex(1.6, 'Parse Quotes with BeautifulSoup')
    
    response = requests.get("http://quotes.toscrape.com/")
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    title_tag = soup.find("title")
    title = title_tag.get_text()
    print("Found Title:")
    print(f"\tTag: {title_tag}")
    print(f"\tText: {title}")
    print()

    quote_tags = soup.find_all("span", class_="text", itemprop="text")
    print("Found Quotes:")
    for q in quote_tags:
        print(f"\t{html.unescape(q.text[1:-1])}")

################################################################################
def ex2_2():
    print_ex(1.6, 'Parse Wikipedia HTML with BeautifulSoup')
    print("Print the first Paragraph of a Wikipedia Article Using BeautifulSoup")
    
    headers = {'User-Agent': "Web Scraping Demo 1.0"}
    webpage = requests.get("https://en.wikipedia.org/wiki/Sheep", headers=headers)
    
    soup = BeautifulSoup(webpage.text, 'html.parser')
    ps = soup.find_all('p')
    print(f"0: {ps[0].text}")
    print(f"1: {ps[1].text}")
    print()
    
    # Get the content div first
    content = soup.find('div', id='mw-content-text')
    ps = content.find_all('p')
    
    def is_body_paragraph(tag: Tag):
        for parent in tag.parents:
            if parent.name == 'table':
                return False
        return True

    print("After filtering:")
    for p in ps:
        if is_body_paragraph(p) and p.text.strip():
            print(p.text)
            break

################################################################################
# Run all examples
if __name__ == "__main__":
    ex2_1()
    ex2_2()