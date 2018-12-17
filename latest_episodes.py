from bs4 import BeautifulSoup
import requests


url = 'http://animeindo.video'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# left_column = soup.find('div', {'id': 'episodes'})


episodes = soup.find('div', {'id': 'episodes'})
episode = episodes.find_all('div', {'class': 'episode'}, recursive=False)

for i in episode:
    # print(('=====' * 35), '\n', i)
    for img_and_a in i:
        a = img_and_a.find('a')
        images = img_and_a.find('img')
        a_href = img_and_a.find('a href')
        print(('=====' * 35), '\n', a)
        # print(('=====' * 35), '\n', a_href)
