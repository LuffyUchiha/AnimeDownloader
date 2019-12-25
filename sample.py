import re
from os import mkdir
from os.path import isdir

import requests

from downloader import downloader

s = "https://www.animefreak.tv/watch/honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-wo-erandeiraremasen"

base_dir = "F:\\Anime\\Ascendence of a Bookworm"
add_dir = ""
current_dir = ""


def getDownloadLink(link):
    r = requests.get(link)
    if r.status_code == requests.codes['ok']:
        sre = re.compile(r'loadVideo.+file: "([^"]+)', re.DOTALL)
        match = sre.findall(r.text)
        print(match)
        url = match[0]
        return url
    else:
        return None


def downloadRange(link, start=1, end=None):
    i = start
    while True:
        url = getDownloadLink(link + "/episode/episode-" + str(i))
        if url is not None:
            out = base_dir + "\\" + str(i) + ".mp4"
            print(out)
            downloader(url, out)
            i += 1
            print(i)
        else:
            break
        if end is not None:
            if i >= end:
                break
    print("Complete")


def multiAnime(links):
    global add_dir, current_dir, base_dir
    for link in links:
        print(links[link])
        (lin, end) = links[link]
        if end is None:
            continue
        else:
            add_dir = link
            current_dir = base_dir + add_dir
            if isdir(base_dir + add_dir):
                current_dir = base_dir + add_dir
            else:
                mkdir(current_dir)
            downloadRange(lin)


# output = r'F:\Anime\a.mp4'
# url=getDownloadLink(s)
# downloader(url,output)
# downloadRange(0, )
downloadRange(s)
