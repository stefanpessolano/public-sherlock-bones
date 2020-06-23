import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as Bsoup

url = 'https://en.wikipedia.org/wiki/List_of_dog_breeds'

client = urlopen(url)
html = client.read()
client.close()

def search(breed):
    breed = breed.lower()
    page = Bsoup(html,"html.parser")
    list = page.findAll("div",{"class":"div-col columns column-width"})

    for item in list:
        test = item.find("a",text = lambda x: x and x.lower()==breed)        
        if(test):
            r = test["href"]
            return r
    return None




    

