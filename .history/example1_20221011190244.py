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
    'a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')

# get the programming language from each repo
wiki_date = wiki.find_all('span', attrs={'aria-hidden': 'true'})
# for each item in p_langauge, print the text
for item in wiki_date:
    print(item.text)

# find each article where class='Box-row'
articles = wiki.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__secondary-item gel-1/1 gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m gs-u-float-left nw-c-top-stories__secondary-item--3 gel-1/5@xxl')
# get length of articles
len(articles)


# get the div that contains data-hpc
articles = wiki.find_all(attrs={
    "gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international": True})  # way one
articles = wiki.find_all('div', attrs={
    'gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international': True})  # way two

# get the name of the repo and print it
article_name = wiki.find_all(
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
