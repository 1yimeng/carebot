import requests
from bs4 import BeautifulSoup
SIGNS = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
     'scorpio', 'sagitarius', 'capricorn', 'aquarius', 'pisces']
URL = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={0}"


def horoscope(sign):
    index = SIGNS.index(sign)
    url = URL.format(str(index + 1))
    response = requests.get(url)

    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    paragraph = soup.find('p')
    return paragraph.text

if __name__ == "__main__":
    horoscope()