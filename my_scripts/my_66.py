# The highest minimum wage as mandated by state law.
import requests
from bs4 import BeautifulSoup
url = 'http://www.dol.gov/whd/minwage/america.htm#Consolidated'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
table = soup.find('table', summary="This is a table of consolidated minimum \
                                    wage rates.")
min_wages = [a.text.split('$')[1]
             for a in table.select('tr > td') if '$' in a.text]
print(max(min_wages))
