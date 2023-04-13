import requests
from bs4 import BeautifulSoup

# define the website URL to crawl
url = 'https://e.vnexpress.net/news/business/industries/tuna-exports-to-uk-triple-4592963.html'

# send a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# extract the text content from the HTML using the get_text() method
text_content = soup.get_text()

# print the text content
print(text_content)