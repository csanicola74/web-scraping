import requests
from bs4 import BeautifulSoup
import pandas as pd


slickdeals = requests.get('https://slickdeals.net/')

# Create a BeautifulSoup object
deals = BeautifulSoup(slickdeals.text, 'html.parser')

# print pretty
print(deals.prettify())


# get the text from each repo
deals.find_all('a', class_='bp-c-card_title bp-c-link')

# find each article where class='Box-row'
deal = deals.find_all(
    'li', class_='bp-p-socialDealCard bp-p-dealCard bp-c-card bp-c-card--border')
# get length of articles
len(deal)


# get the div that contains data-hpc
articles = deals.find_all(
    'ul', class_='dealTiles gridDeals dealTileGridOverrides')


# by looking at the website, can see this is where the info is stored:
# <h1 class=h3 lh-condensed  ---- this is for the name of the repo
# <p1 class=col-9 color-fg-muted my-1 pr-4 ---- this is for the description of the repo

# get the name of the repo and print it
repo_name = deals.find_all('a', class_='bp-c-card_title bp-c-link')
repo_names = []
for item in repo_name:
    print(item.text)
    name = item.text
    # clean name remove whitespace
    name = name.strip()
    # remove new line
    name = name.replace('\n', '')
    # remove all white space
    name = name.replace(' ', '')
    repo_names.append(name)
len(repo_names)

# get the description of the repo and print it
repo_desc = deals.find_all(
    'button', class_='bp-p-storeLink bp-c-linkableButton bp-c-button js-button bp-c-button--link')
repo_descs = []
for item in repo_desc:
    print(item.text)
    desc = item.text
    # clean name remove whitespace
    desc = desc.strip()
    # remove new line
    desc = desc.replace('\n', '')
    repo_descs.append(desc)
len(repo_descs)


# put this together into a dataframe
df = pd.DataFrame({'repo_name': repo_names, 'repo_desc': repo_descs})
