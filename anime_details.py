import re

from bs4 import BeautifulSoup
from datetime import datetime
import requests
start_time = datetime.now()


def anime_descriptions(url_anime_details):
    anime_description_page = BeautifulSoup(url_anime_details.text, 'html.parser')
    title = anime_description_page.find('div', {'class': 'amin_week_box_up1'})
    title = title.text

    # episode_list = anime_description_page.find('div', {'class': 'episode_list'})

    image = anime_description_page.find('div', {'class': 'cat_image'})

    soup = BeautifulSoup(url_anime_details.text, 'html.parser')

    descriptions = soup.find('h3', text='Description:').find_next_sibling()

    pattern = re.compile(r'\w+:\s.*?')

    data = dict(field.split(':') for field in descriptions.find_all(text=pattern))
    # data['Synopsis'] = descriptions.find('p', text="Synopsis:").find_next_sibling("p").get_text()

    # print('Time execution: ', datetime.now() - start_time)

    episode_list_parent = anime_description_page.find('div', {'class': 'desc_box_mid'})
    episode_list_children = episode_list_parent.find_all('div', {'class': 'episode_list'})


    for i in episode_list_children:
        link_to_video =  i.a.get('href')


        url_videos = requests.get(link_to_video)
        # print(url_videos)
        video_link = BeautifulSoup(url_videos.text, 'html.parser')

        video_on_iframe = video_link.find('iframe', allow='encrypted-media' == False)
        # a = video_on_iframe.find('iframe')

        facebook_frame = '<iframe allow="encrypted-media" allowtransparency="true" frameborder="0" height="80" scrolling="no" src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FAnimeindoFans%2F&amp;tabs&amp;width=280&amp;height=180&amp;small_header=true&amp;adapt_container_width=true&amp;hide_cover=true&amp;show_facepile=false&amp;appId=123434497681677" style="border:none;overflow:hidden" width="280"></iframe>'

        if video_on_iframe is not None:
            print(video_on_iframe['src'])





