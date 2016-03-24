# #The total number of publications produced by the U.S. Government Accountability Office 
import re
import requests
from bs4 import BeautifulSoup
url = 'http://www.gao.gov/browse/date/custom'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
title = soup.find('h2', {"class":"scannableTitle"}).text
print(re.search('[,\d]+(?= +items)', title))