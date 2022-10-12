import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get(
    'https://weather.com/weather/tenday/l/2906af11e6df7fe8794d73e25089e8a1c37052441b07f6e71f24b7f72a251641')

# Create a BeautifulSoup object
weather = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(weather.prettify())


# get the text from each repo
weather.find_all(
    'div', class_='temp')


# get the date of each weather
weather_date = weather.find_all(
    'h3',  attrs={'data-testid': 'daypartName'})
# for each item in weather_date, print the text
for item in weather_date:
    print(item.text)

# find each weather where class='Box-row'
articles = weather.find_all(
    'details', class_='DaypartDetails--DayPartDetail--1up3g Disclosure--themeList--25Q0H')
# get length of articles
len(articles)


# get the div that contains data-hpc
weather_10day = weather.find_all(
    'div', class_='DailyForecast--DisclosureList--msYIJ')  # way two

# get the temperature for each day
repo_name = weather.find_all(
    'span', class_='DetailsSummary--highTempValue--3Oteu')
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
repo_desc = weather.find_all(
    'span', class_='DetailsSummary--extendedData--365A_')
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
df
