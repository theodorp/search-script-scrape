#The number of citations that resulted from FDA inspections in fiscal year 2012
import pandas as pd
df = pd.read_csv('http://www.fda.gov/downloads/ICECI/Inspections/UCM346093.csv'
				, skiprows=2
				, usecols=['Firm Name'])

print(len(df))