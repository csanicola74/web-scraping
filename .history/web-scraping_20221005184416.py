from bs4 import BeautifulSoup
import requests
page = requests.get(
    "https://dataquestio.github.io/web-scraping-pages/simple.html")
page

page.status_code

page.content


soup = BeautifulSoup(page.content, ‘html.parser’)

print(soup.prettify())

soup = BeautifulSoup(page.content, 'html.parser')

soup.find_all('p')

soup.find_all(‘p')[0].get_text()

soup.find(‘p')  # find the first instance of the tag
