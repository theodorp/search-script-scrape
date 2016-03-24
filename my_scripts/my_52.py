#The average wage of optomertrists according to the BLS's
# most recent National Occupational Employment and Wage Estimates report 
import requests
from bs4 import BeautifulSoup
url = 'http://www.bls.gov/oes/current/oes_nat.htm'
soup = BeautifulSoup(requests.get(url).content, 'lxml')
table = soup.select('#bodytext table')[0]
t = next(t for t in table.select('tr') if 'Optometrists' in t.text)
print(t.select('td')[-2].text)