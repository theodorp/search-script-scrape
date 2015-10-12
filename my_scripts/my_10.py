# The title of the highest paid California city government position in 2010
import pandas as pd
import requests
import zipfile
from io import BytesIO

years = [2010] # can add more years 
for year in years:
	filename = '%s_City' % year
	url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=%s.zip' % filename
	
	print('Downloading File')
	r = requests.get(url)
	
	print("Unzipping and reading")
	z = zipfile.ZipFile(BytesIO(r.content))
	city = pd.read_csv(z.open(filename+'.csv'), skiprows=4, encoding='latin_1', low_memory=False)

	# Can select any field names that are wanted. 
	print(city.ix[city['Total Wages'].idxmax()][['Entity Name', 'Position', 'Total Wages']])