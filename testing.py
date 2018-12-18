import re

from bs4 import BeautifulSoup
import requests

url = 'http://animeindo.video/category/gundam-build-fighter/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


description = soup.find("h3", text="Description:").find_next_sibling()

pattern = re.compile(r"\w+:\s.*?")

data = dict(field.split(":") for field in description.find_all(text=pattern))
data["Synopsis"] = description.find("p", text="Synopsis:").find_next_sibling("p").get_text()

print(data)
