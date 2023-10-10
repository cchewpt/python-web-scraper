'''
WEB SCRAPER PROJECT
MADE BY : CHIWAPHAT TITSUK
LANGUAGE : PYTHON
DATE : 10/11/2023 (MM/DD/YYYY)
'''

import requests as req
from bs4 import BeautifulSoup as bs

# URL for scraping
url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

# Request url
request = req.get(url)

# Finding title function
def title_function(parser):
    topic = parser.find('h1', id = 'main-content')
    print(topic.text, '\n')

# Finding content function
def content_function(parser):
    content = " "
    article = parser.find('div', class_ ='grid-body')
    paragraphs = article.find_all('p',)
    for paragraph in paragraphs :
        content += "\t" + paragraph.text + '\n\n'
    print(content)

# Finding author function
def author_function(parser):
    author = parser.find('a', rel='author')
    print('By ', author.text)

def update_date(parser):
    date = parser.find('span', class_ = "wpds-c-iKQyrV")
    print(date.text)


##### Main Program #####
# Check status code if request was successful (status code 200)
if request.status_code == 200 :

    # Parsing content
    parse = bs(request.content, 'html.parser')

    # Finding title
    title_function(parse)

    # Finding content
    content_function(parse)

    # Finding author
    author_function(parse)
    # Finding update date
    update_date(parse)

# Check if status code was not 200
else :
    print("URL request was failed!!")

