import requests
from bs4 import BeautifulSoup


def findAnimeLink(animeName):
    searchURL = "https://www.animefreak.tv/home/anime-list"
    r = requests.get(searchURL)
    soup = BeautifulSoup(r.content, 'html.parser')
    soupy = soup.find(id=animeName.lower()[0]).parent
    soupy = soupy.findAll('a')
    links = {}
    for so in soupy:
        if animeName in so.get_text():
            req = requests.get(so['href'])
            print(so['href'])
            soup = BeautifulSoup(req.content, 'html.parser')
            soup = soup.find('ul', class_="check-list")
            index = 1
            soup = soup.findAll('a')
            latestEpi = soup[0].get_text().split()[-1]
            while not latestEpi.isdigit():
                try:
                    latestEpi = soup[index].get_text().split()[-1]
                    index += 1
                except IndexError:
                    latestEpi = None
                    break
            if latestEpi is not None:
                latestEpi = int(latestEpi)
            links[so.get_text()] = (so['href'], latestEpi)
    return links
