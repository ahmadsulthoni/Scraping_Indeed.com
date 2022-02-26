import requests
from bs4 import BeautifulSoup

url = 'https://id.indeed.com/jobs?'

res = requests.get(url)
print(res.status_code)
