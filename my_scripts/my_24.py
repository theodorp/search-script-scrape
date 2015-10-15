#Percentage of NYPD stop-and-frisk reports
# in which the suspect was white in 2014
from io import BytesIO
import zipfile
import requests
import pandas as pd
r = requests.get('http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2014_sqf_csv.zip')
z = zipfile.ZipFile(BytesIO(r.content))
df = pd.read_csv(z.open('2014.csv'), encoding = 'latin-1', low_memory=False) 
print("Percentage of white people stopped and frisked: ", round((len(df.loc[df.race == 'W'])/len(df))*100, 2), '%', sep='')
print("Percentage of black people stopped and frisked: ", round((len(df.loc[df.race == 'B'])/len(df))*100, 2), '%', sep='')