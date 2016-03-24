# The latest release date for T-100 Domestic Market (U.S. Carriers) statistics report 
import re
import requests
from bs4 import BeautifulSoup
url = 'http://www.transtats.bts.gov/releaseinfo.asp'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
row = soup.find('a', text=re.compile('T-100 Domestic Market')).parent.parent
print(row.select('td')[-1].text.split(':')[0])