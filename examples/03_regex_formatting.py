#!/usr/bin/env python3

# Example 3: Regular Expressions for fata formatting
# Learn regex fundamentals and its applications in data cleaning.
# By Chris Casolin, November 2025
# Written for Devsoc Training Program's Intro to Web Scraping Workshop

import re
from helper import print_ex

################################################################################
def ex3_1():
    print_ex(3.1, "Regex Basics - Pattern Matching", topgap=False)
    
    # Sample text data
    text = "Contact us at support@example.com or call 555-123-4567"
    
    print("Original text:")
    print(f"'{text}'")
    print()
    
    # Basic pattern matching with no special characters
    print("1. Literal matching:")
    pattern = "example"
    match = re.search(pattern, text)
    if match:
        print(f"\tFound '{pattern}' at position {match.start()}-{match.end()}")
    print()
    
    print("2. Character classes:")
    # '\d' means digit, it is the same as '[0-9]'
    pattern = r"\d+"  # One or more digits
    matches = re.findall(pattern, text)
    print(f"\tNumbers found: {matches}")
    print()
    
    print("3. Special characters:")
    
    # '\w' means word, it is the same as '[a-zA-Z0-9_]'
    # Matching a simple email pattern
    pattern = r"\w+@\w+\.\w+"
    match = re.search(pattern, text)
    if match:
        print(f"\tEmail found: '{match.group()}'")

################################################################################
def ex3_2():
    print_ex(3.2, "Text Cleaning with Substitution")
    
    messy_texts = [
        "  Too   many    spaces   ",
        "Mixed\nLine\nBreaks\rHere",
        "remove_underscores_from_text",
    ]
    
    print("Cleaning messy text data:")
    print()
    
    for text in messy_texts:
        print(f"Original: {repr(text)}")
        
        # Clean extra whitespace
        cleaned = re.sub(r'\s+', ' ', text)
        print(f"\tStep 1: {repr(cleaned)}")
        
        # Not regex but remove surrounding whitespace
        if re.search("^\s|\s$", cleaned):
            cleaned = cleaned.strip()
            print(f"\tStep 2: {repr(cleaned)}")
        
        # Replace underscores with spaces
        if '_' in cleaned:
            cleaned = re.sub(r'_', ' ', cleaned)
            print(f"\tStep 3: {repr(cleaned)}")
        print()

################################################################################
def ex3_3():
    print_ex(3.3, "Price Extraction")
    
    price_texts = [
        "$19.99",
        "1 000 000 DOLLARS!",
        "Price: $1,234.56 each", 
        "Cost AUD $99.00 (inc tax)",
        "€25.50 or $35.00 USD",
        "Special offer: was $199, now $149.99!",
        "Free shipping on orders over £50.00"
    ]
    
    print("Extracting prices from various text formats:")
    print()
    
    price_pattern = r"([$£€]?(?:\d+[,\.\s]?)+)((?:dollar|pound|euro)s?)?"
    
    # Pattern breakdown:
    # First Part: ([$£€]?(?:\d+[,\.\s]?)+)
    #   [$£€]?      --> Optional currency symbol (dollar, pound, or euro)
    #   (?:...)     --> Non-capturing group
    #   \d+         --> One or more digits
    #   [,\.\s]?    --> Optional separator (comma, period, or space)
    #   (...)+      --> Pattern repeats one or more times
    # Second Part: ((?:dollar|pound|euro)s?)?
    #   (?:...)     --> Non-capturing group
    #   dollar|pound|euro --> Literal text matching currency words
    #   s?          --> Optional 's' for plurals (dollars, pounds, euros)
    #   (...)?      --> Whole thing is optional
    #
    # Combine it all together and we check for any sequence of numbers
    # that may start with a currency symbol and be followed by separators.
    # Optionally, the price may be followed by written currency words
    # like 'dollars', 'pounds', or 'euros'.
    
    for text in price_texts:
        print(f"Text: '{text}'")
        
        # Find all prices
        prices = re.findall(price_pattern, text, re.IGNORECASE)
        for price, curr_str in prices:
            clean_price = re.sub(r'[ ,]', '', price)
            clean_curr_str = curr_str.lower()
            print(clean_price, clean_curr_str)
        print()
        
################################################################################
def ex3_4():
    print_ex(3.4, "Phone Number Extraction")
    
    # https://www.stylemanual.gov.au/grammar-punctuation-and-conventions/numbers-and-measurements/telephone-numbers
    
    # 02 5550 4321                  [A landline number in NSW or the ACT]
    # 0491 570 159                  [An Australian mobile number]
    # 1300 975 707                  [An Australia-wide local-rate number]
    # 13 00 00                      [An alternative Australia-wide local-rate number]
    # 1800 160 401                  [An Australia-wide freephone number]
    # +61 2 5550 4321               [An Australian landline number in international format]
    # +61 491 570 159               [An Australian mobile number in international format]
    
    pattern = "((\(?\+?\d+\)?)?([-\s]?\d+)+)"
    
    # Pattern breakdown:
    # First Part: (\(?\+?\d+\)?)?
    #   \(?         --> Optional open brace
    #   \+?         --> Optional '+' (literal)
    #   \d+         --> One or more digits
    #   \)?         --> Optional closing brace
    #   (...)?      --> Whole thing is optional
    # Second Part: ([-\s]?\d+)+
    #   [-\s]?      --> Optional space or hyphen between numbers
    #   \d+         --> One or more digits
    #   (...)+      --> Pattern repeats one or more times
    #
    # Combine it all together and we check for any sequence of numbers
    # that is separated by spaces or hyphens.
    # Optionally, the firdst numbers may be surrounded by braces and/or
    # start with a '+'.
    
    
    phone_numbers = [
        "555-123-4567",
        "(02) 5550 1234", 
        "my number is +61 412 345 678",
        "(+61) 412 345 678 call now!",
        "call me at 0400 123 456 please",
        "not-a-phone"
    ]
    
    print("Phone numbers to validate:")
    for phone in phone_numbers:
        print(f"\t{phone}")
    print()
    
    print("Results:")
    for phone in phone_numbers:
        match = re.search(pattern, phone)
        if match:
            groups = match.groups()
            print(f"\t{phone:40} -> Groups: {groups}")
        else:
            print(f"\t{phone:40} -> No match")

################################################################################
# Run all examples
if __name__ == "__main__":
    ex3_1()
    ex3_2()
    ex3_3()
    ex3_4()