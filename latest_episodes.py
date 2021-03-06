from bs4 import BeautifulSoup
import threading
import re
import requests
import csv
import time
import json
start = time.time()

url_anime_list = 'http://animeindo.video/anime-list-animeindo/'
anime_list_page = requests.get(url_anime_list)
soup = BeautifulSoup(anime_list_page.text, 'html.parser')

class Anime():
    def get_anime_list(self):

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
                    self.anime_descriptions(url_anime_details)
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

    def anime_descriptions(self, url_anime_details):

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

            video_on_frame = video_link.find_all('iframe', height='380')  ## This means I wanna scrap iframe who has height value 380 . You can also use widht.
            link_array = []
            for link in video_on_frame:  ## Your html has 1 iframe in video_on_frame format.
                get_iframe_url = link['src']  ## find iframe's src
                try:
                    link_array.append(get_iframe_url)  ## add src into a array

                except:
                    link_array.append('Error')

        #=================================================================================================

                DATA = [{
                    'TITLE': TITLE,
                    'IMAGES': IMAGE,
                    'URL_VIDEOS': link_array,
                    'DESCRIPTIONS': DESCRIPTIONS,
                    'SYNOPSIS': SYNOPSIS
                }]


        # with open('result.json', 'a') as outfile:
        #     outfile.write(json.dumps(DATA, sort_keys=True, indent=4))

                print(DATA)

        end = time.time()
        time_execution = 'Time execution: ', end - start
        # print(time_execution)

        # keys = DATA[0].keys()
        # with open('synopsis.csv', 'a') as output_file:
        #     dict_writer = csv.DictWriter(output_file, keys)
        #     dict_writer.writeheader()
        #     dict_writer.writerows(DATA)

    def process(self):
        t1 = threading.Thread(target=self.get_anime_list(), args = (content, link, url_anime_details))
        t2 = threading.Thread(target=self.anime_descriptions, args= (anime_description_page, title, episode_list_parent,
                                                                episode_list_children, link_to_video, url_videos, video_link,
                                                                video_on_iframe, URL_VIDEOS, image, images, IMAGE,
                                                                soup, description, data_descriptions, data_sinopsis, time_execution))

        t1.start()
        t2.start()

        t1.join()
        t2.join()


        return t1, t2

