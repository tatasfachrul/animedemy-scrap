from bs4 import BeautifulSoup
import requests


url = 'http://animeindo.video/anime-list-animeindo'
page = requests.get(url, timeout=10)

soup = BeautifulSoup(page.text, 'html.parser')

mid = soup.find_all('div', {'class': 'amin_box_mid_link'})
del mid[0]

def get_anime_list():
    try:
        for i in mid:
            anime_list = {
                'title': i.text,
                'link:': i
            }
            print(anime_list)
    except:
        print('Exception')

get_anime_list()



