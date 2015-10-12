#From 2010 to 2013, the change in median cost of health, dental, and vision coverage for California city employees 
import requests
import pandas as pd
import zipfile
from io import BytesIO
### 2013_url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=2013_City.zip'

hdv = []
years = [2010,2013]

for year in years:
	filename = '%s_City' % year
	url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=%s.zip' % filename
	
	print('Downloading %s File' % year) 
	r = requests.get(url)
	
	print("Unzipping and reading")
	z = zipfile.ZipFile(BytesIO(r.content))
	city = pd.read_csv(z.open(filename+'.csv'), skiprows=4, encoding='latin_1', usecols=['Health Dental Vision'],low_memory=False)

	# Can select any field names that are wanted. 
	med = city['Health Dental Vision'].median()
	print("Median for %s:" % year, med)
	hdv.append(med)

print("Difference: ", hdv[1]-hdv[0])