import requests
page = requests.get(
    "https://dataquestio.github.io/web-scraping-pages/simple.html")
page

page.status_code

page.content
