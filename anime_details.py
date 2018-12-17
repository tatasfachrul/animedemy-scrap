from bs4 import BeautifulSoup


def anime_descriptions(url_anime_details):
    anime_description_page = BeautifulSoup(url_anime_details.text, 'html.parser')
    title = anime_description_page.find('div', {'class': 'amin_week_box_up1'})
    title = title.text

    a = anime_description_page.find('div', {'class': 'episode_list'})
    b = a
    print('======' * 30, b)