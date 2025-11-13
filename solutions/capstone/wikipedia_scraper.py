#!/usr/bin/env python3

# Wikipedia Scraper written by Chris Casolin, November 2025
# Written for Devsoc Training Program's Intro to Web Scraping Workshop
# Program accepts user search terms and retrieves Wikipedia articles.
# It handles disambiguation pages and search results by allowing user selection.
# It also extracts key facts from articles using regex pattern matching.

import requests
import re
import sys
import textwrap
from bs4 import BeautifulSoup, Tag

class WikipediaScraper:
    def __init__(self):
        self.WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"
        self.SEARCH_URL = "https://en.wikipedia.org/w/index.php/"
        self.HEADERS = {
            "User-Agent": "Wikipedia Workshop Scraper 1.0 (Educational Use)"
        }
        # Config
        self.PAGE_SIZE = 10
        self.TEXT_WRAP_WIDTH = 100
        self.FACT_LIMIT = 4
        
        # Commands
        self.QUIT_COMMANDS = ['q', 'quit', 'exit']
        self.CANCEL_COMMANDS = ['c', 'cancel']
        self.MORE_COMMANDS = ['m', 'more']
    
    def print_heading(self, str):
        print("-"*self.TEXT_WRAP_WIDTH)
        print(" " * int((self.TEXT_WRAP_WIDTH - len(str)) / 2) + str)
        print("-"*self.TEXT_WRAP_WIDTH)

    # Display prompt asking user for a new search term
    def prompt_new_search(self):
        print("\nWhat would you like to learn about?")
        
    
    # Check if user input is a command to quit the program
    def is_stop_command(self, input):
        return input.strip() in self.QUIT_COMMANDS
    
    
    # Check if user input is a command to cancel current operation
    def is_cancel_command(self, input):
        return input in self.CANCEL_COMMANDS
    
    
    # Check if user input is a command to see more results
    def is_more_command(self, input):
        return input in self.MORE_COMMANDS
    
    
    # Get user input and handle quit commands
    def handle_user_input(self):
        line = input("> ")
        if self.is_stop_command(line): self.stop()
        return line
    
    
    # Stop the program and exit
    def stop(self):
        print("Bye!")
        sys.exit(0)
    
    
    # Convert user input into a valid Wikipedia query format
    # Replaces spaces with underscores for URL compatibility
    def form_query(self, line):
        return '_'.join(line.split())
    
    
    # Make HTTP request to URL with optional parameters
    # Returns response object if successful, None if error
    def get_response(self, url, params={}):
        try:
            response = requests.get(url, params=params, headers=self.HEADERS)
            if response.status_code == 200:
                return response
            else:
                print("Received:", response)
            
        except Exception as e:
            print('error: ', e)
    
    
    # Extract title and body content from Wikipedia article page
    # Filters out content from tables and infoboxes to get main article text
    # Returns tuple of (title, list_of_paragraphs)
    def extract_page_paragraphs(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.find('div', id='mw-content-text')
        ps = content.find_all('p')
        
        raw_title = soup.find('title')
        title = raw_title.text.split('-')[0].strip()
        
        def is_body_paragraph(tag: Tag):
            for parent in tag.parents:
                if parent.name == 'table':
                    return False
            return True

        content = []
        for p in ps:
            if is_body_paragraph(p) and p.text.strip():
                content.append(p.text.strip())

        return (title, content)
    
    
    # Extract links from disambiguation pages
    # Returns list of anchor tags
    def extract_disambiguation_links(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.find('div', id='mw-content-text')
        links = content.select('li a')
        return links
    
    
    # Display paginated list of options to user
    # Returns selected index or None if cancelled
    def paginate(self, options):
        pos = 0
        prompt = True
        while True:
            if prompt:
                for i, option in enumerate(options[pos:pos+self.PAGE_SIZE], pos + 1):
                    print(f"\t{i}. {option}")
                print("Which topic would you like to explore?")
                
            try:
                print("See more (m), Cancel (c), Or enter a line number:")
                line = self.handle_user_input()
                if self.is_more_command(line):
                    if pos + self.PAGE_SIZE < len(options):
                        pos = pos + self.PAGE_SIZE
                        prompt = True
                    else:
                        print('No More to Show')
                        prompt = False
                    continue
                elif self.is_cancel_command(line):
                    return
                else:
                    n = int(line)
                    if n < 1 or n > len(options): raise ValueError
                    return n - 1
            except (EOFError, KeyboardInterrupt):
                self.stop()
            except ValueError:
                print('Invalid Selection')
                prompt = False
                continue
         
         
    # Handle a list of Wikipedia links by showing them to user and processing selection
    def handle_links_list(self, list):
        if list:
            options = [r.get('title') for r in list]
            selected = self.paginate(options)
            # Assume valid index (handled in paginate)
            if selected is not None:
                href = list[selected].get('href')
                query = href.split('/')[-1]
                self.perform_search(query)
            else:
                self.prompt_new_search()
        else:
            print("\tNo results found")
            self.prompt_new_search()
        
        
    # Handle Wikipedia disambiguation pages by extracting topic links
    def handle_disambiguation_page(self, page_html):
        topics = self.extract_disambiguation_links(page_html)
        self.handle_links_list(topics)
    
    
    # Check if current page is a disambiguation page
    # Looks for "Category:Disambiguation_pages" in the page categories
    def is_disambiguation_page(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        catlinks = soup.find('div', id='catlinks')
        links = catlinks.find_all('a')
        for l in links:
            if "Category:Disambiguation_pages" in l.get('href'):
                return True
        return False

        
    # Handle main Wikipedia content pages
    # Displays article title and first paragraph, or redirects to disambiguation        
    def handle_content_page(self, page_html):
        title, body = self.extract_page_paragraphs(page_html)
        print(f"Found: {title}")
        self.print_heading("Overview")
        # If page is a disambiguation page then we recurse
        if self.is_disambiguation_page(page_html):
            self.handle_disambiguation_page(page_html)
        # Otherwise, it is a normal page. So print overview paragraph and key facts
        else:
            wrapped_first = textwrap.fill(body[0], width=self.TEXT_WRAP_WIDTH)
            print(wrapped_first)
            facts = self.extract_key_facts(' '.join(body[:3]))  # First 3 paragraphs
            self.display_facts(facts)
            self.prompt_new_search()
            
    # Extract search result links from Wikipedia search results page
    # Returns list of anchor tags from search result items
    def extract_search_results_links(self, page_html):
        try:
            soup = BeautifulSoup(page_html, 'html.parser')
            content = soup.find('ul', class_='mw-search-results')
            links = content.select('li', class_="mw-search-result")
            links = [l.find('a') for l in links]
            return links
        except AttributeError:
            return []
    
    
    # Handle Wikipedia search results page when no exact match is found
    # Shows list of suggested articles for user to choose from
    def handle_search_result_page(self, query, page_html):
        print(f"No page for '{query}'. Found these search results!")
        results = self.extract_search_results_links(page_html)
        self.handle_links_list(results)
            

    # Extract interesting facts from Wikipedia article text using regex patterns
    # Returns dictionary categorised facts:
    # - dates
    # - money
    # - measurements
    # - quotes
    # - locations
    def extract_key_facts(self, article_text):
        facts = {
            'Dates': set(),
            'Money': set(),
            'Measurements': set(),
            'Quotes': set(),
            'Locations': set()
        }
        
        # Dates
        date_patterns = [
            # March 15, 2024
            r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}',
            # 15 March 2024
            r'\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}',
            # 1991 or 1991-2024
            r'\d{4}(?:[-–]\d{4})?',
            # 03/15/24 or 03/15/2024
            r'\d{1,2}/\d{1,2}/\d{2,4}',
            # born 1991, founded in 2001
            r'(?:born|died|founded|established|created|released)\s+(?:in\s+)?\d{4}'
        ]
        
        for pattern in date_patterns:
            matches = re.findall(pattern, article_text, re.IGNORECASE)
            facts['Dates'].update(matches)
        
        # Money
        money_patterns = [
            r'([$£€¥](?:\d+[,\.\s]?)+)',
            r'((?:\d+[,\.\s]?)+)\s*((?:dollar|pound|euro|yen)s?)',
        ]
        
        for pattern in money_patterns:
            matches = re.findall(pattern, article_text, re.IGNORECASE)
            matches = [''.join(m) for m in matches]
            facts['Money'].update(matches)
    
        
        # Measurements
        measurement_patterns = [
            # Distances
            r'\d+(?:,\d{3})*\s*(?:metres?|feet|kilometers?|kilometres?|miles?|inches?|cm|mm|km)',
            # Weights
            r'\d+(?:,\d{3})*\s*(?:kg|kilograms?|pounds?|lbs?|tonnes?|tons?)',
            # People
            r'\d+(?:,\d{3})*\s*(?:people|inhabitants|residents|population|students|members|employees)',
            # Large numbers with units
            r'\d+(?:\.\d+)?\s*(?:million|billion|thousand|hundred)\s*(?:people|square|years?|acres?|cm|mm|m|km)',
            # Area
            r'\d+(?:\.\d+)?\s*(?:square\s+)?(?:kilometres?|kilometers?|miles?|acres?)'
        ]
        
        for pattern in measurement_patterns:
            matches = re.findall(pattern, article_text, re.IGNORECASE)
            facts['Measurements'].update(matches)
        
        # Quotes
        quote_patterns = [
            r'\s"([^"]{10,120})"\s',
            r"\s'([^']{10,120})'\s",
            r'\s“([^“]{10,120})”\s'
        ]
        
        for pattern in quote_patterns:
            matches = re.findall(pattern, article_text)
            facts['Quotes'].update(matches)
        
        # Locations
        location_patterns = [
            # "in Paris, France"
            r'\bin\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*),\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            # "in|at|from England"
            r'\b(?:in|at)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
        ]
        
        for pattern in location_patterns:
            matches = re.findall(pattern, article_text)
            if matches:
                if isinstance(matches[0], tuple):
                    facts['Locations'].update([f"{m[0]}, {m[1]}" for m in matches])
                else:
                    facts['Locations'].update(matches)
        
        return facts
    
    
    # Display extracted facts in a nicely formatted way
    def display_facts(self, facts):
        found = False
        self.print_heading("Key Facts")
        for title, values in facts.items():
            if values:
                found = True
                print(f"{title}:")
                # Sort by longest fact because its probably more interesting.
                # Take only the first few to prevent overkill.
                sorted_facts = sorted(list(values), key=lambda x: len(x), reverse=True)
                limited_facts = sorted_facts[:self.FACT_LIMIT]
                for i, v in enumerate(limited_facts, 1):
                    print(f"\t{i}. {v}")
                    
        if not found:
            print("No facts found. Try a different article!")
    
    
    # Main search method that coordinates the entire search process
    # Handles both direct page matches and search result pages
    def perform_search(self, query):
        print(f"Searching Wikipedia for '{query}'")
        
        # First try searching for the query.
        # Wikipedia will redirect of it finds a page with an exact match.
        params = {
            'search': query
        }
        response = self.get_response(self.SEARCH_URL, params=params)
        
        # Check nothing went wrong
        if not response:
            print(f"Sorry! No page exists for '{query}'. Please try again!")
            return

        # If no redirect was made, expand on the search results.
        if '?search=' in response.url:
            self.handle_search_result_page(query, response.text)
        # Otherwise go to the found page
        elif '/wiki/' in response.url:
            self.handle_content_page(response.text)
        # We shouldnt get here.
        else:
            print(f"Unsupported Page Type: {response.url}")
    
    
    # Main program loop that handles user interaction
    # Continuously prompts for search terms and processes them
    def run(self):
        print("Welcome to Wikipedia Scraper!")
        print("Type 'q' at any time to quit")
        print("\nWhat would you like to learn about?")
        while True:
            try:
                line = self.handle_user_input()
                query = self.form_query(line)
                self.perform_search(query)
                    
            except (EOFError, KeyboardInterrupt):
                self.stop()


def main():
    scraper = WikipediaScraper()
    scraper.run()


if __name__ == "__main__":
    main()