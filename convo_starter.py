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

