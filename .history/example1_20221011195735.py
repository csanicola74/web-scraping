import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import json


page = requests.get(
    'https://www.indeed.com/l-Long-Island,-NY-jobs.html?vjk=50391d8af59670ab')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


# get the text from each repo
soup.find_all(
    'h2', class_='jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0')


# get the programming language from each repo
p_langauge = soup.find_all(
    'span', class_='companyName')
# for each item in p_langauge, print the text
for item in p_langauge:
    print(item.text)

# find each article where class='Box-row'
articles = soup.find_all('article', class_='Box-row')
# get length of articles
len(articles)


# get the div that contains data-hpc
articles = soup.find_all(attrs={"data-hpc": True})  # way one
articles = soup.find_all('div', attrs={'data-hpc': True})  # way two


# by looking at the website, can see this is where the info is stored:
# <h1 class=h3 lh-condensed  ---- this is for the name of the repo
# <p1 class=col-9 color-fg-muted my-1 pr-4 ---- this is for the description of the repo

# get the name of the repo and print it
repo_name = soup.find_all('h1', class_='h3 lh-condensed')
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
repo_desc = soup.find_all('p', class_='col-9 color-fg-muted my-1 pr-4')
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
