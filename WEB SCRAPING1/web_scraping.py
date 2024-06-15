import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



# 
html1 = urllib.request.urlopen(url).read()
soup1 = BeautifulSoup(html1, 'html.parser')
# 
# Retrieve all of the h1 tags
tags1 = soup1.find_all('h1')
for tag1 in tags1:
    print(tag1.text)    # This will print the text within the h1 tag

print(soup1.prettify())   # This will print the entire html document in a structured format
print(soup1.title)        # This will print the title tag
print(soup1.title.string)  # This will print the title tag without the tag
print(soup1.title.parent.name)  # This will print the parent tag of the title tag
for link1 in soup1.find_all('p'):  # This will print all the p tags
    print(link1.get('class', None))  # This will print the class of the p tag
for link in soup1.find_all('a'):     # This will print all the a tags
    print(link.get('href', None))    # This will print the href of the a tag
print(soup1.get_text())             # This will print the text of the entire html document

