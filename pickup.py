import requests
from bs4 import BeautifulSoup, NavigableString

URL = 'https://athlonsports.com/pick-up-lines-funny'

response = requests.get(URL)
html = response.content
soup_pickup = BeautifulSoup(html, 'html.parser')
all_lines = soup_pickup.find('div', {"class": "field-item even"}) 
# print(all_lines)
text_list = []
all_li = all_lines.find_all('li')
for li in all_li:
    if isinstance(li, NavigableString):
        continue
    if li.text != '':
        text_list.append(li.text)
#print(text_list)