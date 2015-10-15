#The names of the committees that Sen.
# Barbara Boxer currently serves on 
import requests
from bs4 import BeautifulSoup, SoupStrainer
r = requests.get('http://www.senate.gov/general/committee_assignments/assignments.htm')
soup = BeautifulSoup(r.content, 'lxml', parse_only=SoupStrainer("td"))
bboxer = soup.find('a', text='Boxer, Barbara').parent.findNext('td').text
print(', '.join(bboxer.strip().split('\n\n')))