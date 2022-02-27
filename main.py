import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
params = {
    'q' : 'Python Developer',
    'l' : 'New York State',

}
headers = { 'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 '}

res = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())