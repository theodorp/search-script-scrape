#Number of sponsored bills by Rep. Nancy Pelosi
# that were vetoed by the President
import re
import requests
from bs4 import BeautifulSoup
url = 'https://www.congress.gov/member/nancy-pelosi/P000197'
atts = {'q': '{"sponsorship":"sponsored","bill-status":"veto"}'}
r = requests.get(url, params=atts)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find('span', {'class':'results-number'}).text.split()[2])
