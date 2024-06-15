import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://x.com/home.html"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())