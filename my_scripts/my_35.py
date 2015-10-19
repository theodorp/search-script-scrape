#Most viewed data set on New York state's open data portal as of this month
import requests
from bs4 import BeautifulSoup
url_base = 'https://data.ny.gov/browse'
url_payload = {'sortBy':'most_accessed', 'sortPeriod':'month','utf8':'✓'}
r = requests.get(url_base, params=url_payload)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.select('tr.item .titleLine a')[0].text)