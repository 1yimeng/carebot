import requests
from bs4 import BeautifulSoup, NavigableString

def get_convo():
    URL = 'https://www.generatorslist.com/random/questions/random-conversation-starters'

    response = requests.get(URL)
    html = response.content
    soup_pickup = BeautifulSoup(html, 'html.parser')
    # print(all_lines)
    convo_starters = []
    # ps = soup_pickup.find_all('p')
    div = soup_pickup.find('div', id='results')
    for p in div:
        if isinstance(p, NavigableString):
            continue
        if p.text != '':
            convo_starters.append(p.text)
    return convo_starters

def get_never_have_I_ever():
    URL = 'https://www.generatorslist.com/random/questions/never-have-i-ever'

    response = requests.get(URL)
    html = response.content
    soup_convo = BeautifulSoup(html, 'html.parser')
    divs = soup_convo.find('div', id='results')
    for div in divs:
        if isinstance(div, NavigableString):
            continue
        return div.text

