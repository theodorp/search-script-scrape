#The dropout rate for all of Santa Clara County
# high schools, according to the latest cohort data in CALPADS 
from io import BytesIO
import requests
import pandas as pd

print("Getting prefix.")
santa_clara = pd.read_table('ftp://ftp.cde.ca.gov/demo/schlname/pubschls.txt', usecols=['CDSCode', 'County'])
CDS = santa_clara.loc[santa_clara.County == 'Santa Clara', 'CDSCode'].values
SC_prefix = int(CDS[0].astype(str)[0:2])
print("Santa Clara prefix is:", SC_prefix)

print("Getting Average Cohort Dropout Rate")
url = 'http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=All&cYear=2013-14&cCat=Cohort&Cpage=filescohort'
r = requests.get(url)
df = pd.read_table(BytesIO(r.content), usecols=['CDS', 'Name', 'Cohort Dropout Rate'])
df['prefix'] = df['CDS'].map(lambda x: int(str(x)[0:2]))
df = df.loc[df.prefix == SC_prefix]
print('Average Cohort Dropout Rate:', df['Cohort Dropout Rate'].mean())