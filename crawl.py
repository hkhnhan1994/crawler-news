import requests
from bs4 import BeautifulSoup
import csv

# define the URL of the news website you want to crawl
url = 'https://e.vnexpress.net/news/business/industries/tuna-exports-to-uk-triple-4592963.html'

# send a GET request to the website and get the HTML content
response = requests.get(url)
xml_content = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(xml_content, 'xml')

# find all the article elements on the page
articles = soup.find_all("div", class_="main_detail_page")

# define the filename and fieldnames for the CSV file
filename = 'news.csv'
fieldnames = ['Title', 'Author', 'Content']

# open the CSV file for writing
with open(filename, 'w', newline='') as csvfile:
    # create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # write the header row to the CSV file
    writer.writeheader()
    
    # loop through each article and extract relevant information
    for article in articles:
        # extract the article title
        title = article.find('h1', class_='title_post').getText()
        
        # extract the article author
        author = article.find('a').getText()
        
        # extract the article content
        content = article.find('div', class_='fck_detail').getText()
        
        # write the extracted information to the CSV file
        writer.writerow({'Title': title, 'Author': author, 'Content': content})