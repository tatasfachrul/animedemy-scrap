import json
from bs4 import BeautifulSoup
import requests

from anime_details import anime_descriptions

url_anime_list = 'http://animeindo.video/anime-list-animeindo/'
anime_list_page = requests.get(url_anime_list)
soup = BeautifulSoup(anime_list_page.text, 'html.parser')


def get_anime_list():

    content = soup.find_all('div', {'class': 'amin_box_mid_link'})

    out_list = []

    try:
        del content[0]
        for i in content:
            link =  i.find_all('a', href=True)

            try:
                link = link[0]['href']
                if link == 'href=':
                    link = 'URL IS EMPTY'
            except IndexError:
                link = 'URL NOT FOUND'
                continue

            try:
                url_anime_details = requests.get(link)
                anime_descriptions(url_anime_details)
            except:
                continue

    except Exception as e:
        print('Exception', e)


get_anime_list()

