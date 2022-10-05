# $ pip3 install beautifulsoup4

from bs4 import BeautifulSoup
import requests

########################
##  GETTING THE PAGE  ##
########################

page = requests.get(
    "https://dataquestio.github.io/web-scraping-pages/simple.html")
page

page.status_code

page.content

#########################################
##  PARSING A PAGE WITH BEAUTIFULSOUP  ##
#########################################

soup = BeautifulSoup(page.content, ‘html.parser’)

print(soup.prettify())

###########################################
##  FINDING INSTANCES OF A SPECIFIC TAG  ##
###########################################

soup = BeautifulSoup(page.content, 'html.parser')

soup.find_all('p')

soup.find_all(‘p')[0].get_text()

soup.find(‘p')  # find the first instance of the tag

###############################
##  FINDING BY CLASS AND ID  ##
###############################

soup = BeautifulSoup(page.content, 'html.parser')

soup.find_all('p', class_=‘outer-text')

soup.find_all(class_=“outer-text")

soup.find_all(id="first")

###############################
##  USING CUSTOM ATTRIBUTES  ##
###############################

soup = BeautifulSoup(page.content, 'html.parser')


soup.find_all(attrs={"data-hpc": True})
// GitHub example - trending repos, where there is no class name to go off of
