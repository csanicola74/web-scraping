import requests
from bs4 import BeautifulSoup
import pandas as pd


slickdeals = requests.get('https://slickdeals.net/')

# Create a BeautifulSoup object
deals = BeautifulSoup(slickdeals.text, 'html.parser')

# print pretty
print(deals.prettify())


# get the text from deal listing
deals.find_all('a', class_='bp-c-card_title bp-c-link')


# get the website for each deal
website = deals.find_all(
    'button', class_='bp-p-storeLink bp-c-linkableButton bp-c-button js-button bp-c-button--link')
# for each website name, print the text
for item in website:
    print(item.text)

# find each deal where class='li'
deal = deals.find_all(
    'li', class_='bp-p-socialDealCard bp-p-dealCard bp-c-card bp-c-card--border')
# get length of deals
len(deal)


# get the div that contains data-hpc
deal = deals.find_all(
    'ul', class_='dealTiles gridDeals dealTileGridOverrides')

# get the name of the deals and print it
deal_name = deals.find_all('a', class_='bp-c-card_title bp-c-link')
deal_names = []
for item in deal_name:
    print(item.text)
    name = item.text
    # clean name remove whitespace
    name = name.strip()
    # remove new line
    name = name.replace('\n', '')
    # remove all white space
    name = name.replace(' ', '')
    deal_names.append(name)
len(deal_names)

# get the website of the deal and print it
deal_site = deals.find_all(
    'button', class_='bp-p-storeLink bp-c-linkableButton bp-c-button js-button bp-c-button--link')
deal_sites = []
for item in deal_site:
    print(item.text)
    desc = item.text
    # clean name remove whitespace
    desc = desc.strip()
    # remove new line
    desc = desc.replace('\n', '')
    deal_sites.append(desc)
len(deal_sites)


# put this together into a dataframe
slickdeals_listings = pd.DataFrame(
    {'deal_names': deal_names, 'deal_sites': deal_sites})
slickdeals_listings.to_csv('data/slickdeals_listings.csv')
slickdeals_listings
