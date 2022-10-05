from bs4 import BeautifulSoup
import requests
page = requests.get(
    "https://dataquestio.github.io/web-scraping-pages/simple.html")
page

page.status_code

page.content


soup = BeautifulSoup(page.content, ‘html.parser’)

print(soup.prettify())
