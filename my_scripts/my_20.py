#The number of OSHA enforcement inspections
# involving Wal-Mart in California since 2014
import requests
from bs4 import BeautifulSoup
url_base = 'https://www.osha.gov/pls/imis/establishment.search'
url_args = {
	'establishment':'wal-mart',
	'State':'CA',
	'officetype':'all',
	'Office':'all',
	'p_case':'all',
	'p_violations_exist':'all',
	'startmonth':'01',
	'startday':'01',
	'startyear':'2014',
	'endmonth':'10',
	'endday':'14',
	'endyear':'2015'
}

r = requests.get(url_base, params=url_args)
soup = BeautifulSoup(r.content, 'lxml')
# this was going to be a list-comp, but decided agaisnt
for entry in soup.find_all('div',{'class':'text-right'}):
	if 'Results' in entry.text:
		print(entry.text.split()[-1])
