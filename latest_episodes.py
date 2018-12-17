from bs4 import BeautifulSoup
import requests


url = 'http://animeindo.video'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# left_column = soup.find('div', {'id': 'episodes'})


li = soup.find('div', {'id': 'episodes'})
children = li.find_all('div', {'class': 'episode'})
for child in children:
    print(child)