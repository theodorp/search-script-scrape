# Number of FDA-approved prescription drugs with GlaxoSmithKline
# as the applicant holder
import re
import requests
from bs4 import BeautifulSoup

formurl = 'http://www.accessdata.fda.gov/scripts/cder/ob/docs/tempah.cfm'
post_params = {'Sponsor': 'GlaxoSmithKline', 'table1': 'OB_Rx'}
r = requests.post(formurl, data=post_params)

soup = BeautifulSoup(r.content, 'lxml')

print(soup.find(text=re.compile("Displaying records")).strip())
