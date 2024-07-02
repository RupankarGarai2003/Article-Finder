import requests  # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML content
from googlesearch import search  # Import search function for Google search
from newspaper import Article  # Import Article class for processing articles
import nltk  # Import nltk for natural language processing
from datetime import datetime  # Import datetime for date handling
import re  # Import re for regular expressions

# Download required nltk data
nltk.download('punkt', quiet=True)

def extract_with_newspaper(url):
    try:
        article = Article(url)  # Create an Article object
        article.download()  # Download the article content
        article.parse()  # Parse the article content
        article.nlp()  # Perform natural language processing on the article

        return {
            'title': article.title,  # Extract the title
            'date': article.publish_date,  # Extract the publish date
            'summary': article.summary,  # Extract the summary
            'image_urls': [article.top_image] if article.top_image else [],  # Extract the top image URL
            'video_urls': article.movies,  # Extract video URLs
            'url': url  # Include the original URL
        }
    except:
        return None  # Return None if any error occurs

def extract_with_custom_scraper(url):
    try:
        response = requests.get(url, timeout=10)  # Make an HTTP GET request
        soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content

        title = soup.find('h1').text.strip() if soup.find('h1') else "Title not found"  # Extract the title

        date = soup.find('time')  # Find the date element
        if date:
            date = date.get('datetime') or date.text  # Extract the date
        else:
            date_patterns = [r'\d{4}-\d{2}-\d{2}', r'\d{2}/\d{2}/\d{4}', r'\w+ \d{1,2}, \d{4}']  # Define date patterns
            for pattern in date_patterns:
                match = re.search(pattern, response.text)  # Search for date patterns
                if match:
                    date = match.group()  # Extract the date if found
                    break
            else:
                date = None  # Set date to None if not found

        paragraphs = soup.find_all('p')  # Find all paragraph elements
        content = ' '.join([p.text for p in paragraphs])  # Combine paragraph texts
        summary = content[:500] + "..." if len(content) > 500 else content  # Create a summary

        images = soup.find_all('img', src=True)  # Find all image elements with src attribute
        image_urls = [img['src'] for img in images if img['src'].startswith('http')][:3]  # Extract image URLs

        videos = soup.find_all('video', src=True)  # Find all video elements with src attribute
        video_urls = [video['src'] for video in videos if video['src'].startswith('http')][:3]  # Extract video URLs

        return {
            'title': title,  # Include the title
            'date': date,  # Include the date
            'summary': summary,  # Include the summary
            'image_urls': image_urls,  # Include image URLs
            'video_urls': video_urls,  # Include video URLs
            'url': url  # Include the original URL
        }
    except:
        return None  # Return None if any error occurs

def search_and_extract_articles(search_term, num_results=5):
    articles = []  # Initialize an empty list to store articles
    try:
        for url in search(search_term, num_results=num_results):  # Perform a Google search
            article = extract_with_newspaper(url) or extract_with_custom_scraper(url)  # Extract article using both methods
            if article:
                articles.append(article)  # Append the article if extraction was successful
    except Exception as e:
        print(f"Error in search: {str(e)}")  # Print any errors during search
    return articles  # Return the list of articles

# Example usage:
search_term = input("Please enter the topic you want to search about: ")  # Prompt user for search term
article_results = search_and_extract_articles(search_term)  # Search and extract articles

if article_results:
    for article in article_results:
        print(f"Title: {article['title']}")  # Print article title
        print(f"Date: {article['date']}")  # Print article date
        print(f"Summary: {article['summary'][:200]}...")  # Print truncated summary
        print(f"Image URLs: {', '.join(article['image_urls'])}")  # Print image URLs
        print(f"Video URLs: {', '.join(article['video_urls'])}")  # Print video URLs
        print(f"Source URL: {article['url']}")  # Print source URL
        print("\n---\n")
else:
    print("No articles found or an error occurred.")  # Print message if no articles found or an error occurred
