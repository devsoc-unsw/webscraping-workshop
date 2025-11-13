# Web Scraping Workshop

Learn the fundamentals of web scraping with Python

## Workshop Overview

This workshop teaches web scraping from the ground up, starting with basic HTTP requests and progressing to advanced HTML parsing and data extraction techniques. Students will build a complete Wikipedia scraper that handles real-world challenges like disambiguation pages, search results, and structured data extraction.

## Learning Objectives

By the end of this workshop, you will be able to:
- Make HTTP requests to APIs and web pages
- Parse HTML content using BeautifulSoup
- Extract structured data using regular expressions
- Handle edge cases like redirects and error responses
- Build a complete web scraping application with user interaction

## Prerequisites

- Basic Python knowledge (functions, loops, conditionals)
- Familiarity with command line usage
- Text editor or IDE (VS Code recommended)

## Setup Instructions

1. **Clone or download this workshop repository**
2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   . .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Workshop Structure

### Examples

#### 1. Basic HTTP Requests (`examples/01_basic_requests.py`)
- Making GET requests to APIs
- Handling URL parameters
- Introduction to raw HTML scraping
- Basic error handling and status codes

**Run:** `python3 examples/01_basic_requests.py`

#### 2. HTML Parsing with BeautifulSoup (`examples/02_beautifulsoup_basics.py`)
- Why regex isn't sufficient for HTML parsing
- BeautifulSoup basics: finding elements by tags, classes, and IDs
- Extracting text and attributes
- Comparing regex vs. proper HTML parsing

**Run:** `python3 examples/02_beautifulsoup_basics.py`

#### 3. Regular Expressions for Data Formatting (`examples/03_regex_formatting.py`)
- Regex fundamentals and syntax
- Pattern matching for data extraction
- Text cleaning and normalization
- Practical regex patterns for common data types

**Run:** `python3 examples/03_regex_formatting.py`

### Capstone Project: Wikipedia Scraper

Build a complete Wikipedia article scraper that demonstrates all learned concepts.

#### Features:
- **Search Wikipedia articles** by topic
- **Handle disambiguation pages** with user selection
- **Process search results** when no exact match exists
- **Extract key facts** using regex patterns (dates, money, measurements, quotes, locations)
- **Interactive interface** with pagination and user commands
- **Robust error handling** for network issues and edge cases

#### Files:
- `solutions/capstone/wikipedia_scraper.py` - **Complete solution** for reference
- `capstone/template.wikipedia_scraper.py` - **Student template** with TODO instructions

### Template Structure

The template provides a structured approach to building the scraper:

**Basic Functions (Complete First):**

1. `get_response()` - HTTP requests and error handling
2. `extract_page_paragraphs()` - HTML parsing with BeautifulSoup

**Advanced Functions (Complete After Basic Works):**

3. `is_disambiguation_page()` - Detect special page types
4. `extract()_disambiguation_links()` - Extract topic links
5. `extract_search_results_links()` - Handle search results
6. `extract_key_facts()` - Regex-based data extraction

## Getting Started

1. **Work through examples in order:**
   ```bash
   python3 examples/01_basic_requests.py
   python3 examples/02_beautifulsoup_basics.py
   python3 examples/03_regex_formatting.py
   ```

2. **Start the capstone project:**
   ```bash
   cp capstone/template.wikipedia_scraper.py capstone/wikipedia_scraper.py
   chmod u+x capstone/wikipedia_scraper.py
   ```

3. **Test your progress:**
   ```bash
   ./capstone/wikipedia_scraper.py
   ```

4. **Compare with the solution:**
   ```bash
   ./solutions/capstone/wikipedia_scraper.py
   ```

## Testing Your Implementation

### Basic Functions Test:
- Try searching: `Python (programming language)`
- Should display article title and first paragraph

### Advanced Functions Test:
- Try searching: `Python` (disambiguation page)
- Try searching: `asdfghijk` (search results page)
- Any article should show extracted facts

## Dependencies

- **requests** - HTTP library for making web requests
- **beautifulsoup4** - HTML parsing and navigation

## Tips for Success

1. **Complete examples in order** - each builds on the previous
2. **Read the TODO comments carefully** - they provide step-by-step guidance
3. **Test frequently** - verify each function works before moving on
4. **Use print statements** for debugging - see what data you're getting
5. **Check the solution** if stuck, but try implementing first
6. **Experiment** - try different Wikipedia topics to test edge cases

## Learning Resources

- [Requests Documentation](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Regular Expressions Guide](https://docs.python.org/3/library/re.html)
