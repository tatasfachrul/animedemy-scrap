from bs4 import BeautifulSoup
import requests

url = 'http://animeindo.video/'

page = requests.get(url)

print(page)

