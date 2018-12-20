import re
from bs4 import BeautifulSoup
from datetime import datetime
import requests


start_time = datetime.now()


DATA = []
TITLE = []
URL_VIDEO = []
IMAGE = None
DESCRIPTIONS = None


object_videos_url = {}

def anime_descriptions(url_anime_details):
    anime_description_page = BeautifulSoup(url_anime_details.text, 'html.parser')


    title = anime_description_page.find('div', {'class': 'amin_week_box_up1'})
    title = title.text

    TITLE = title

    # episode_list = anime_description_page.find('div', {'class': 'episode_list'})

    episode_list_parent = anime_description_page.find('div', {'class': 'desc_box_mid'})
    episode_list_children = episode_list_parent.find_all('div', {'class': 'episode_list'})


    for i in episode_list_children:
        link_to_video = i.a.get('href')

        url_videos = requests.get(link_to_video)

        video_link = BeautifulSoup(url_videos.text, 'html.parser')

        video_on_iframe = video_link.find('iframe', allow='encrypted-media' == False)

        if video_on_iframe is not None:
            URL_VIDEO = video_on_iframe['src']

            object_videos_url = {
                    'URL_VIDEO': URL_VIDEO
            }

            # print(object_videos_url)


    image = anime_description_page.find('div', {'class': 'cat_image'})
    images = image.find_all('img')

    for i in images:
        IMAGE = i['src']

    soup = BeautifulSoup(url_anime_details.text, 'html.parser')

    # first locate the container with the desired fields
    description = soup.find("h3", text="Description:").find_next_sibling()

    # get all the ":"-separated fields into a dictionary
    pattern = re.compile(r"\w+:\s.*?")

    data_descriptions = dict(field.split(":") for field in description.find_all(text=pattern))
    # data_descriptions["Synopsis"] = description.find("p", text="Synopsis:").find_next_sibling("p").get_text()
    # print('Time execution: ', datetime.now() - start_time)

    DESCRIPTIONS = data_descriptions


    DATA = [
        TITLE, {
            'IMAGES': IMAGE,
            'URL_VIDEO': URL_VIDEO,
            'DESCRIPTIONS': DESCRIPTIONS
        }
    ]
    print(DATA)
    print('Time execution: ', datetime.now() - start_time)


