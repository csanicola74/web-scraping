from bs4 import BeautifulSoup
import requests
import pandas as pd


session = requests.Session()
session.get(r'https://www.rottentomatoes.com/')


def grab_reviews(genre_link):
    source = requests.get(genre_link).text
    soup = BeautifulSoup(source, 'html')

    movie_reviews = {'ratings': [], 'critics': []}

    for m in soup.find_all('table', class_='table')[0].find_all('a', href=True):
        url = 'https://www.rottentomatoes.com/' + m['href']
        sub_source = session.get(url)
        sub_soup = BeautifulSoup(sub_source, 'html')
        try:
            critic = sub_soup.find(
                'div', class_='col-sm-12 tomato-info hidden-xs')
            c = critic.text.split('Critics Consensus:')[1]
        except Exception as e:
            c = None

        try:
            rating = sub_soup.find('div', class_='superPageFontColor')
            r = rating.text.split('Average Rating:')[1].split('/')[0]
        except Exception as e:
            r = None

        movie_reviews['ratings'].append(r)
        movie_reviews['critics'].append(c)

    return movie_reviews


source = requests.get('https://www.rottentomatoes.com/top/').text
soup = BeautifulSoup(source, 'html')

all_movie_reviews = {'ratings': [], 'critics': []}

source = requests.get('https://www.rottentomatoes.com/top/').text
soup = BeautifulSoup(source, 'html')
for link in soup.find('ul', class_='genrelist').find_all('a', href=True):
    genre_link = 'https://www.rottentomatoes.com/' + link['href']
    movie_reviews = grab_reviews(genre_link)
    all_movie_reviews['ratings'] = all_movie_reviews['ratings'] + \
        movie_reviews['ratings']
    all_movie_reviews['critics'] = all_movie_reviews['critics'] + \
        movie_reviews['critics']
