import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as Bsoup

def getInfo(breed):
    url = 'https://en.wikipedia.org' + breed.lower()
    client = urlopen(url)
    html = client.read()
    client.close()

    page = Bsoup(html,"html.parser")

    info = page.find("table",{"class":"infobox biota"})
    imageLink = info.find("a",{"class":"image"}).img["src"]

    r = {"breed": breed, "image": imageLink, "url": url}

    return r
