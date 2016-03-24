# The highest salary possible for a White House staffmember in 2014
import requests
import pandas as pd

url = 'https://open.whitehouse.gov/resource/i9g8-9web.csv'
df = pd.read_csv(url)
sal = df['Salary'].map(lambda x: float(x.replace('$', ''))).max()

print('$'+str(sal))
