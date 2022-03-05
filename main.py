import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
site = 'https://www.indeed.com'
params = {
    'q' : 'Python Developer',
    'l' : 'New York State',

}
#agar program tidak terdeteksi sebagai bot
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

    total_pages = []
    #scraping step
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul','pagination-list')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total

def get_all_item():
    params = {
        'q' : 'Python Developer',
        'l' : 'New York State',

    }
    res = requests.get(url, params=params, headers=headers)

    with open('temp/res.html','w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')

    #scaraping prosess
    contents = soup.find_all('table', 'jobCard_mainContent big6_visualChanges')

    for item in contents:
        title = item.find('h2', 'jobTitle').text
        company = item.find('span','companyName')
        company_name = company.text
        try:
            company_link = site + company.find('a')['href']
        except:
            company_link = 'Link is Not Available'
        print(company_link)
if __name__ == '__main__':
    get_all_item()

