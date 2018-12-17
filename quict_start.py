from bs4 import BeautifulSoup
import requests

url = 'https://jadwalsholat.pkpu.or.id/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


# print(soup.find_all('p')[4].get_text()) # find tag 'P' with index array number '4'

''' # find tags by class or id '''
# print(soup.find_all(class_='table_highlight'))
# print(soup.find_all('tr', class_='table_highlight'))
# print(soup.find_all(id='third'))

