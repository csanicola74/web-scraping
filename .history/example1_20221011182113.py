import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://www.bbc.com/news')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


# get the title from each repo
soup.find_all(
    'a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')

# get the programming language from each repo
p_langauge = soup.find_all('span', attrs={'itemprop': 'programmingLanguage'})
# for each item in p_langauge, print the text
for item in p_langauge:
    print(item.text)

<a href = "/news/world/europe" class = "gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state" aria-label = "From Europe" > <span aria-hidden = "true" > Europe < /span > </a >

# find each article where class='Box-row'
articles = soup.find_all(
    'div', class_='gel-layout__item nw-c-top-stories__secondary-item gel-1/1 gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m gs-u-float-left nw-c-top-stories__secondary-item--3 gel-1/5@xxl')
# get length of articles
len(articles)


# get the div that contains data-hpc
articles = soup.find_all(attrs={
                         "gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international": True})  # way one
articles = soup.find_all('div', attrs={
                         'gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international': True})  # way two


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
