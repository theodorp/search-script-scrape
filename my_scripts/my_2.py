# The name of the most recently added dataset on data.gov
import requests
from bs4 import BeautifulSoup
r = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc').content
soup = BeautifulSoup(r, 'html.parser').find_all('h3')[0]
print(soup.text.strip())