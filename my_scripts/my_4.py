# The number of librarian-related job positions that the federal government is currently hiring for
import requests
r = requests.get('https://data.usajobs.gov/api/jobs?series=1410')
print(r.json()["TotalJobs"])