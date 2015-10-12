#The number of armored carrier bank robberies recorded by the FBI in 2014
from io import BytesIO
import requests
from PyPDF2 import PdfFileReader
import re

url = "https://www.fbi.gov/stats-services/publications/bank-crime-statistics-2014/bank-crime-statistics-2014"
r = requests.get(url)
pdf = PdfFileReader(BytesIO(r.content))
text = pdf.getPage(0).extractText()
robberies = re.search("Armored Carrier Companies +(\d+)", text).group(1)
print("Armored Carrier Companies: ", robberies)