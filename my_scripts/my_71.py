# The percent increase in number of babies named Archer nationwide in
# 2010 compared to 2000, according to the Social Security Administration
import zipfile
from io import BytesIO
import pandas as pd
import requests
url = 'https://www.ssa.gov/oact/babynames/names.zip'

r = requests.get(url)
z = zipfile.ZipFile(BytesIO(r.content))

df10 = pd.read_csv(z.open('yob2010.txt'), names=['name', 'gender', 'count'])

df00 = pd.read_csv(z.open('yob2000.txt'), names=['name', 'gender', 'count'])

count10 = df10.loc[df10.name == 'Archer']['count'].sum()
count00 = df00.loc[df00.name == 'Archer']['count'].sum()

print((count10-count00)/count00*100)
