import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
params = {
    'q' : 'Python Developer',
    'l' : 'New York State',

}
headers = { 'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 '}

res = requests.get(url, params=params, headers=headers)


#mendapatkan total page secara dinamis
def get_total_pages():
    params = {
    'q' : 'Python Developer',
    'l' : 'New York State',

}
    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html','w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    #scraping step
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())


if __name__ == '__main__':
    get_total_pages()