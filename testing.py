from bs4 import BeautifulSoup

html = '''
<a href="http://something" title="Development of the Python language and website">Core Development</a>
<a href="http://something.com" title="Development of the Python language and website">Core Development</a>
'''

soup = BeautifulSoup(html)

for a in soup.find_all('a', href=True):
    print(a['href'])