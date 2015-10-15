#The name of the California school with the highest number 
# of girls enrolled in kindergarten, according to the CA
# Dept. of Education's latest enrollment data file. 
import pandas as pd
url = 'http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2014-15&cCat=Enrollment&cPage=filesenr.asp'
df = pd.read_table(url, usecols=['SCHOOL', 'GENDER', 'KDGN'])
#Use CDS_CODE since School names can be the same for multiple schools
females = df.loc[df.GENDER == 'F'].groupby(['CDS_CODE', 'SCHOOL'])['KDGN'].sum()
print(females.idxmax()[1])