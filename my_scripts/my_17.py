#In the "Justice News" RSS feed maintained by the Justice 
# Department, the number of items published on a Friday 
import requests
from bs4 import BeautifulSoup
url = 'http://www.justice.gov/feeds/opa/justice-news.xml'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
pubdates = [entry.text.split(',')[0] for entry in soup.find_all('pubdate')]
print(len([day for day in pubdates if day.strip() == 'Fri']))