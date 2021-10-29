import requests
from bs4 import BeautifulSoup, NavigableString

def pickupline():
    URL = 'https://www.cosmopolitan.com/sex-love/a36534574/flirty-pick-up-lines-for-texting/'
    response = requests.get(URL)
    html = response.content
    soup_pickup = BeautifulSoup(html, 'html.parser')
    # print(all_lines)
    text_list = []
    all_ul = soup_pickup.find('ol')
    for li in all_ul:
        if isinstance(li, NavigableString):
            continue
        if li.text != '':
            text_list.append(li.text)
    return text_list
# print(text_list)