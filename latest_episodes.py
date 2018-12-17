from bs4 import BeautifulSoup
import requests

url = 'http://animeindo.video/anime-list-animeindo/'
page = requests.get(url, timeout=10)

soup = BeautifulSoup(page.text, 'html.parser')

mid = soup.find_all('div', {'class': 'amin_box_mid_link'})

def get_anime_list():
    try:
        del mid[0]
        for i in mid:
            link =  i.find_all('a', href=True)

            title = i.text
            link = link[0]['href']
            # print('TITLE: ', title, 'LINK: ', link)

            title_and_link = {
                'title': title,
                'link': link
            }

            print(title_and_link)

    except Exception as e:
        print('Exception', e)


get_anime_list()





