# The total number of babies named Odin born in Colorado according to the Social Security Administration
from io import BytesIO
import zipfile
import pandas as pd
import requests
url = 'https://www.ssa.gov/oact/babynames/state/namesbystate.zip'
r = requests.get(url)
z = zipfile.ZipFile(BytesIO(r.content))

df = pd.read_csv(z.open('OH.TXT'), 
                 names=['State', 'Gender', 'Year', 'Name', 'Count'],
                 usecols=['Name', 'Count'])

print(sum(df[df['Name'] == 'Odin']['Count']))
