# We want to grab all the info from our webpage
# This is web-scraping
# Some libraries are gonna be used
from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# use ___ as file -> do smth
# make lxml type of file from the html_file, which is
# simple.html

# print(soup.prettify())
# prettify is a method from the soup library
# which prettifies the output
# we access the different parts of the document
# by find func
for article in soup.find_all('div', class_='article'):
    headline = article.h2.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
# we can access the parts of wha we got
