import pandas as pd  # library for data analysis
import requests  # library to handle requests
from bs4 import BeautifulSoup  # library to parse HTML documents

# get the response in the form of html
wikiurl = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
table_class = "wikitable sortable jquery-tablesorter"
response = requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.find('table', {'class': "wikitable"})
