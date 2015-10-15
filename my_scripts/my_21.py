#The current humidity level at Great 
# Smoky Mountains National Park
import requests
from bs4 import BeautifulSoup
url = 'http://www.nature.nps.gov/air/WebCams/parks/grsmcam/grsmcam.cfm'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml').find('div', text="Humidity")
print(soup.text, "is", soup.next_sibling.next_sibling.text)