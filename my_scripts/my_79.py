# The change in total airline revenues from baggage fees, from 2013 to 2014 
import requests
from bs4 import BeautifulSoup
base_url = 'http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/subject_areas/airline_information/baggage_fees/html/%d.html'
# for year in [2013, 2014]:
year = {2013: 0, 2014:0}
for y in year.keys():
    url = base_url % y
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    val = int(soup.select('tbody > tr > td > b')[-1].text.replace(',', '')) * 1000
    year[y] = val

print(year[2014] - year[2013])