#!/usr/bin/env python3

# Wikipedia Scraper - Student Template
# Complete the stubbed functions to build a Wikipedia article scraper.

# BASIC FUNCTIONS (Complete these first):
# 1. get_response() - Make HTTP requests to Wikipedia
# 2. extract_page_paragraphs() - Extract article content using BeautifulSoup

# ADVANCED FUNCTIONS (Complete after basic scraper works):
# 3. is_disambiguation_page() - Detect disambiguation pages
# 4. extract_disambiguation_links() - Extract links from disambiguation pages  
# 5. extract_search_results_links() - Extract links from search result pages
# 6. extract_key_facts() - Extract structured data using regex patterns

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


    # ========================================================================
    # BASIC FUNCTIONS - Complete these first to get basic scraping working
    # ========================================================================
    
    # BASIC FUNCTION 1: Make HTTP request to URL with optional parameters
    # TODO: Implement HTTP requests with proper error handling
    def get_response(self, url, params={}):
        """
        Make an HTTP GET request to Wikipedia.
        
        TODO: Complete this function:
        1. Use requests.get() with url, params=params, and headers=self.HEADERS
        2. Check if response.status_code == 200 (success)
        3. If successful, return the response object
        4. If failed, print the response status and return None
        5. Handle any exceptions (network errors, timeouts) by printing the error and returning None
        
        Args:
            url (str): The URL to request
            params (dict): Optional URL parameters (like search terms)
            
        Returns:
            requests.Response or None: Response object if successful, None if failed
            
        Test with: https://en.wikipedia.org/wiki/Python_(programming_language)
        """
        # YOUR CODE HERE
        pass
    
    
    # BASIC FUNCTION 2: Extract title and body content from Wikipedia article page
    # TODO: Use BeautifulSoup to parse HTML and extract article information
    def extract_page_paragraphs(self, page):
        """
        Extract the title and main content paragraphs from Wikipedia HTML.
        
        TODO: Complete this function:
        1. Create BeautifulSoup object: soup = BeautifulSoup(page, 'html.parser')
        2. Find main content div: content = soup.find
            Hint look for an id called 'mw-content-text'
        3. Find all paragraph tags: ps = content.find_all('p')
        4. Extract title from: raw_title = soup.find('title')
        5. Filter paragraphs to exclude those inside tables
            - Hint: access parent tags with .parents
            - Note: This check will work most of the time. But, there are other edge cases.
              Try your scraper on "Daintree_Rainforest" and see what you get.
        6. Return tuple: (title, list_of_paragraph_texts)
    
        
        Args:
            page (str): Raw HTML from Wikipedia page
            
        Returns:
            tuple: (title_string, list_of_paragraph_texts)
        """
        # YOUR CODE HERE
        pass


    # ========================================================================
    # ADVANCED FUNCTIONS - Complete these after basic scraper works
    # ========================================================================
    
    # ADVANCED FUNCTION 3: Check if current page is a disambiguation page
    # TODO: Detect disambiguation pages by looking at page categories
    def is_disambiguation_page(self, page_html):
        """
        Detect if the current page is a disambiguation page.
        
        TODO: Complete this function:
        Hints:
            - Use beautiful soup
            - Look for the div with id 'catlinks'
        
        
        Args:
            page_html (str): Raw HTML from Wikipedia page
            
        Returns:
            bool: True if disambiguation page, False otherwise
        """
        # YOUR CODE HERE
        pass
    
    
    # ADVANCED FUNCTION 4: Extract links from disambiguation pages
    # TODO: Get topic links for user to choose from
    def extract_disambiguation_links(self, page):
        """
        Extract topic links from a disambiguation page.
        
        TODO: Complete this function:
        
        Hints:
            - looks for main content box (like in extract_page_paragraphs())
            - use bs4 .select() descendent selector
            - https://www.educative.io/answers/beautiful-soup-select
        
        Args:
            page (str): Raw HTML from disambiguation page
            
        Returns:
            list: List of anchor tag elements (<a> tags)
        """
        # YOUR CODE HERE
        pass
    
    
    # ADVANCED FUNCTION 5: Extract search result links from search results page
    # TODO: Get search result links when no exact match is found
    def extract_search_results_links(self, page_html):
        """
        Extract search result links from Wikipedia search page.
        
        TODO: Complete this function:
        Hints:
            - Look through the html of a wikipedia search result page.
                - Chrome dev tools are good for this.
                - Or curl -sL <link> > tempfile
            - Try to find something specific to search result anchor tags that you
              can leverage with bs4.
        
        Args:
            page_html (str): Raw HTML from search results page
            
        Returns:
            list: List of anchor tag elements, empty list if none found
        """
        # YOUR CODE HERE
        pass
    
    
    # ADVANCED FUNCTION 6: Extract interesting facts using regex patterns
    # TODO: Use regex to find structured data in article text
    def extract_key_facts(self, article_text):
        """
        Extract interesting facts from article text using regex patterns.
        
        TODO: Complete this function:
        Hints:
            - This is a very difficult exercise.
            - If you are not familiar with regex, feel free to take the patterns
              from previous examples.
            - Also feel free to add your own fact categories to the dictionary!
            - Within each set, the extracted facts should be strings.
            - set.update(<list>) will add an entire list to a set.
        
        Args:
            article_text (str): Combined text from article paragraphs
            
        Returns:
            dict: Dictionary with sets of extracted facts for each category
        """
        # YOUR CODE HERE
        # Initialize the facts dictionary
        facts = {
            'Dates': set(),
            'Money': set(),
            'Measurements': set(),
            'Quotes': set(),
            'Locations': set()
        }
        
        # Add your regex patterns and extraction logic here
        
        return facts


    # ========================================================================
    # COMPLETED FUNCTIONS - These are already implemented for you
    #   It may be useful to read over some of them to see how your functions
    #   interact.
    # ========================================================================
    
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
    
    
    # Handle Wikipedia search results page when no exact match is found
    # Shows list of suggested articles for user to choose from
    def handle_search_result_page(self, query, page_html):
        print(f"No page for '{query}'. Found these search results!")
        results = self.extract_search_results_links(page_html)
        self.handle_links_list(results)
            
    
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