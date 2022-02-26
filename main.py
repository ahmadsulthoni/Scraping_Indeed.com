import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

res = requests.get(url)
print(res.headers)
