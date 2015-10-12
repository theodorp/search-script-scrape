#The number of workplace fatalities at reported to the 
# federal and state OSHA in the latest fiscal year
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
# To find CSV Url
base_url = 'https://www.osha.gov'
r = requests.get(base_url+'/dep/fatcat/dep_fatcat.html')
soup = BeautifulSoup(r.content, 'lxml')

csv_url = soup.find('a', {'href':re.compile('.csv')}).get('href')
df = pd.read_csv(base_url+csv_url)
# df = pd.read_csv('https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv')

fatalities = df.loc[df['Fatality or Catastrophe'] == 'Fatality', 'Fatality or Catastrophe']
print(len(fatalities))