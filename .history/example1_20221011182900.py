import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://www.bbc.com/news')

# Create a BeautifulSoup object
bbc = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(bbc.prettify())


# get the title from each repo
bbc.find_all(
    'a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')

# get the programming language from each repo
bbc_location = bbc.find_all('span', attrs={'aria-hidden': 'true'})
# for each item in p_langauge, print the text
for item in bbc_location:
    print(item.text)

# find each article where class='Box-row'
articles = bbc.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__secondary-item gel-1/1 gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m gs-u-float-left nw-c-top-stories__secondary-item--3 gel-1/5@xxl')
# get length of articles
len(articles)


# get the div that contains data-hpc
articles = bbc.find_all(attrs={
    "gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international": True})  # way one
articles = bbc.find_all('div', attrs={
    'gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international': True})  # way two

# get the name of the repo and print it
article_name = bbc.find_all(
    'h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')
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
article_summary = bbc.find_all(
    'a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')
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
