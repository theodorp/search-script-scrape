#Number of times Rep. Darrell Issa's remarks have made it onto the Congressional Record 
import requests
from bs4 import BeautifulSoup
url = 'https://www.congress.gov/search'
atts = {'source':'congrecord','crHouseMemberRemarks':'Issa, Darrell E. [R-CA]'}
r = requests.get(url, params=atts)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find('span', {'id':'facetItemsourceCongressional_Recordcount'}).text)