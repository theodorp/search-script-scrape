#The title of the most recent decision handed down by the U.S. Supreme Court 
import requests
from bs4 import BeautifulSoup
url = 'http://www.supremecourt.gov/opinions/slipopinions.aspx'
soup = BeautifulSoup(requests.get(url).content, 'lxml')
print(soup.select("table.table-bordered > tr > td")[3].text)