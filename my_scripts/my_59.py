# The number of university-related datasets currently listed at data.gov
import requests
from bs4 import BeautifulSoup

url = 'http://catalog.data.gov/dataset?organization_type=University&sort=metadata_created+desc&q='
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find('div', {'class': 'new-results'}).text.strip())
