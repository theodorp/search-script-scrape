#Total number of visitors to the White House in 2012 
import zipfile
from io import BytesIO
import pandas as pd
import requests
url = 'https://www.whitehouse.gov/sites/default/files/disclosures/whitehouse-waves-2012.csv_.zip'
print("Making Request - Downloading Data")
r = requests.get(url)
z = zipfile.ZipFile(BytesIO(r.content))
print("Opening Zip into Dataframe")
df = pd.read_csv(z.open('WhiteHouse-WAVES-2012.csv'), usecols=['Total_People', 'APPT_START_DATE'], low_memory=False)
# df = pd.read_csv('/Users/theodor/Downloads/WhiteHouse-WAVES-2012.csv', usecols=['Total_People', 'APPT_START_DATE'], low_memory=False)

# Convert column to numeric, coerce errors to NaN, then drop them 
df['Total_People'] = pd.to_numeric(df['Total_People'], errors='coerce')
df = df.dropna()

# Remove duplications, and sum 'total people' column
df = df.drop_duplicates(['Total_People', 'APPT_START_DATE'])

print('Total Visitors : ', df['Total_People'].sum())