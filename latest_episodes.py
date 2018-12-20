from bs4 import BeautifulSoup
import threading
import re
import requests
import csv
import time
start = time.time()

url_anime_list = 'http://animeindo.video/anime-list-animeindo/'
anime_list_page = requests.get(url_anime_list)
soup = BeautifulSoup(anime_list_page.text, 'html.parser')


def get_anime_list():

    global content, link, url_anime_details

    content = soup.find_all('div', {'class': 'amin_box_mid_link'})

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



# =================================================================================


DATA = []
TITLE = []
URL_VIDEOS = []
URL_VIDEO = []
IMAGE = None
DESCRIPTIONS = None
SYNOPSIS = None

object_videos_url = {}

def anime_descriptions(url_anime_details):

    global anime_description_page, title, episode_list_parent, episode_list_children, \
        link_to_video, url_videos, video_link, video_on_iframe, URL_VIDEOS, image, images, \
        IMAGE, soup, description, data_descriptions, time_execution, data_sinopsis

    anime_description_page = BeautifulSoup(url_anime_details.text, 'html.parser')


    title = anime_description_page.find('div', {'class': 'amin_week_box_up1'})
    title = title.text

    TITLE = title

    # episode_list = anime_description_page.find('div', {'class': 'episode_list'})


    image = anime_description_page.find('div', {'class': 'cat_image'})
    images = image.find_all('img')

    for i in images:
        IMAGE = i['src']

    soup = BeautifulSoup(url_anime_details.text, 'html.parser')

# ===============================================================================================================================
    # # first locate the container with the desired fields
    description = soup.find("h3", text="Description:").find_next_sibling()
    #
    # get all the ":"-separated fields into a dictionary
    pattern = re.compile(r"\w+:\s.*?")
    #
    data_descriptions = dict(field.split(":") for field in description.find_all(text=pattern))
    # # data_descriptions["Synopsis"] = description.find("p", text="Synopsis:").find_next_sibling("p").get_text()
# ===============================================================================================================================

    # sinopsis = soup.find('div', text="Sinopsis:").find_next_sibling()
    # data_sinopsis = dict(field.split(":") for field in sinopsis.find_all(text=pattern))
    data_sinopsis = soup.find('div', {'align': 'justify'})
    SYNOPSIS = data_sinopsis.text

    DESCRIPTIONS = data_descriptions

    #=================================================================================================
    episode_list_parent = anime_description_page.find('div', {'class': 'desc_box_mid'})
    episode_list_children = episode_list_parent.find_all('div', {'class': 'episode_list'})

    for i in episode_list_children:
        link_to_video = i.a.get('href')

        url_videos = requests.get(link_to_video)

        video_link = BeautifulSoup(url_videos.text, 'html.parser')

        video_on_iframe = video_link.find('iframe', allow='encrypted-media' == False)
        if video_on_iframe is not None:
            URL_VIDEOS = video_on_iframe['src']
            # print(URL_VIDEOS)
    # URL_VIDEO.append(URL_VIDEOS)
    #         print(URL_VIDEOS)
    #=================================================================================================

    DATA = [
        TITLE, {
            'IMAGES': IMAGE,
            'URL_VIDEOS': URL_VIDEOS,
            'DESCRIPTIONS': DESCRIPTIONS,
            'SYNOPSIS': SYNOPSIS
        }
    ]
    # print(DATA)

    end = time.time()
    time_execution = 'Time execution: ', end - start
    # print(time_execution)

    with open('list.csv', 'w') as f:
        for dict in DATA:
            for key, value in dict.items():
                text = key + ',' + value + '\n'
                f.writelines(text)


def process():
    t1 = threading.Thread(target=get_anime_list(), args = (content, link, url_anime_details))
    t2 = threading.Thread(target=anime_descriptions, args= (anime_description_page, title, episode_list_parent,
                                                            episode_list_children, link_to_video, url_videos, video_link,
                                                            video_on_iframe, URL_VIDEOS, image, images, IMAGE,
                                                            soup, description, data_descriptions, data_sinopsis, time_execution))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

