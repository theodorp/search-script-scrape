#From 2010 to 2013, the change in median cost of health, dental, and vision coverage for California city employees 
import requests
import pandas as pd
import zipfile
from io import BytesIO
### 2013_url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=2013_City.zip'
url_base = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file='

year = "2013"
url_year = '%s_City' % year
r = requests.get(url_base + url_year + '.zip')
z = zipfile.ZipFile(BytesIO(r.content))
city2013 = pd.read_csv(z.open(url_year + '.csv'), skiprows=2)

print(city2013.head())