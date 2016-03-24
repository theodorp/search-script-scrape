#The difference in total White House
# staffmember salaries in 2014 versus 2010 
import pandas as pd
url2010 = 'https://open.whitehouse.gov/api/views/rcp4-3y7g/rows.csv?accessType=DOWNLOAD'
url2014 = 'https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD'

def salary(url):
	df = pd.read_csv(url, usecols=['Salary'])
	return df['Salary'].apply(lambda x: float(x[1:])).sum()

print('2014 salary - 2010 salary: ', salary(url2014)-salary(url2010))