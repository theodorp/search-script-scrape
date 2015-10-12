#How much did the state of California collect in property taxes, 
# according to the U.S. Census 2013 Annual Survey of State Government Tax Collections?
import zipfile 
from io import BytesIO
import pandas as pd
import requests
url = 'http://www2.census.gov/govs/statetax/state_tax_collections.zip'
r = requests.get(url).content
z = zipfile.ZipFile(BytesIO(r))

df = pd.read_excel(z.open('STC_Historical_DB.xls'))
ca_name = "CA STATE GOVT"
year = 2014
paid = df.loc[(df.Year == year) & (df.Name == ca_name), 'T01'].values
print("%s paid $%i in %i" % (ca_name, paid[0]*1000, year))