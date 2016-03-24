#In the most recently transcribed Supreme Court
# argument, the number of times laughter broke out
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader
from io import BytesIO
url = 'http://www.supremecourt.gov/oral_arguments/'
r = requests.get(url + 'argument_transcript.aspx')
soup = BeautifulSoup(r.content, 'lxml')
url_pdf = soup.select('table.datatables > tr > td > a')[0]['href']
r2 = requests.get(url+url_pdf)
pdf = PdfFileReader(BytesIO(r2.content))
print(pdf)
