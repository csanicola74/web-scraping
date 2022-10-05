# $ pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd

films = requests.get(
    'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films')
books = requests.get(
    'https://books.toscrape.com')

# Create a BeautifulSoup object
soup_films = BeautifulSoup(films.text, 'html.parser')
soup_books = BeautifulSoup(books.text, 'html.parser')

# print pretty
print(soup_films.prettify())
print(soup_books.prettify())

# get the text from each repo
soup_films.find_all('p', class_='col-9 color-fg-muted my-1 pr-4')
soup_books.find_all('p', class_='col-9 color-fg-muted my-1 pr-4')

# get the programming language from each repo
p_language_films = soup_films.find_all(
    'span', attrs={'itemprop': 'programmingLanguage'})
p_language_books = soup_books.find_all(
    'span', attrs={'itemprop': 'programmingLanguage'})

# for each item in p_language, print the text
for item in p_language_films:
    print(item.text)
for item in p_language_books:
    print(item.text)

# find each article where class='Box-row'
articles_films = soup_films.find_all('article', class_='Box-row')
articles_books = soup_books.find_all('article', class_='Box-row')

# get length of articles
len(articles_films)
len(articles_books)

# get the div that contains data-hpc
articles = soup_films.find_all(attrs={"data-hpc": True})  # way one
articles = soup_books.find_all('div', attrs={'data-hpc': True})  # way two

articles = soup_films.find_all(attrs={"data-hpc": True})  # way one
articles = soup_books.find_all('div', attrs={'data-hpc': True})  # way two

# by looking at the website, can see this is where the info is stored:
# <h1 class=h3 lh-condensed  ---- this is for the name of the repo
# <p1 class=col-9 color-fg-muted my-1 pr-4 ---- this is for the description of the repo

# get the name of the film and print it
repo_name_films = soup_films.find_all('h1', class_='h3 lh-condensed')
repo_names_films = []
for item in repo_name_films:
    print(item.text)
    name = item.text
    # clean name remove whitespace
    name = name.strip()
    # remove new line
    name = name.replace('\n', '')
    # remove all white space
    name = name.replace(' ', '')
    repo_names_films.append(name)
len(repo_names_films)

repo_name_books = soup_books.find_all('h1', class_='h3 lh-condensed')
repo_names_books = []
for item in repo_name_books:
    print(item.text)
    name = item.text
    # clean name remove whitespace
    name = name.strip()
    # remove new line
    name = name.replace('\n', '')
    # remove all white space
    name = name.replace(' ', '')
    repo_names_books.append(name)
len(repo_names_books)

# get the description of the repo and print it
repo_desc_films = soup_films.find_all(
    'p', class_='col-9 color-fg-muted my-1 pr-4')
repo_descs_films = []
for item in repo_desc_films:
    print(item.text)
    desc = item.text
    # clean name remove whitespace
    desc = desc.strip()
    # remove new line
    desc = desc.replace('\n', '')
    repo_descs_films.append(desc)
len(repo_descs_films)

repo_desc_books = soup_books.find_all(
    'p', class_='col-9 color-fg-muted my-1 pr-4')
repo_descs_books = []
for item in repo_desc_books:
    print(item.text)
    desc = item.text
    # clean name remove whitespace
    desc = desc.strip()
    # remove new line
    desc = desc.replace('\n', '')
    repo_descs_books.append(desc)
len(repo_descs_books)

# put this together into a dataframe
df_films = pd.DataFrame(
    {'repo_name': repo_names_films, 'repo_desc': repo_descs_films})
df_films
df_films.to_csv(
    '/dataFiles/df_films.csv')

df_books = pd.DataFrame(
    {'repo_name': repo_names_books, 'repo_desc': repo_descs_books})
df_books
df_books.to_csv(
    '/dataFiles/df_books.csv')
