import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://en.wikipedia.org/wiki/Portal:Current_events')

# Create a BeautifulSoup object
wiki = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(wiki.prettify())


# get the title from each repo
wiki.find_all(
    'b')

# get the programming language from each repo
wiki_date = wiki.find_all('span', class_='summary')
# for each item in wiki_date, print the text
for item in wiki_date:
    print(item.text)

# find each article where class='Box-row'
articles = wiki.find_all(
    'li')
# get length of articles
len(articles)


# get the name of the repo and print it
article_name = wiki.find_all('b')
article_name = []
for item in article_name:
    print(item.text)
    name = item.text
    # clean name remove whitespace
    name = name.strip()
    # remove new line
    name = name.replace('\n', '')
    # remove all white space
    name = name.replace(' ', '')
    article_name.append(name)
len(article_name)

# get the description of the repo and print it
article_summary = wiki.find_all(
    'p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
article_summary = []
for item in article_summary:
    print(item.text)
    desc = item.text
    # clean name remove whitespace
    desc = desc.strip()
    # remove new line
    desc = desc.replace('\n', '')
    article_summary.append(desc)
len(article_summary)

# put this together into a dataframe
df = pd.DataFrame({'repo_name': article_name, 'repo_desc': article_summary})
