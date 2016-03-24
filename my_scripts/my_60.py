# Number of chapters in Title 20 (Education) of the United States Code
import re
import requests
from bs4 import BeautifulSoup

url = 'http://uscode.house.gov/view.xhtml?path=/prelim@title20&edition=prelim'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# print(soup.find_all('div', {'class': "three-column-analysis-style-content-left"})[-1].text)
print(soup.find_all('h3', {'class': "chapter-head"})[-1].text)
