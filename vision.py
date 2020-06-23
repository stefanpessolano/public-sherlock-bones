import os, io
from google.cloud import vision
from google.cloud.vision import types
import wikiscraper as wiki
import datascraper as data

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'visonServiceKey.json'

client = vision.ImageAnnotatorClient();


#File that is going to be analyzed
def upload(file):
    # fileName = r'corgi.jpg'
    # path = f'.\images\{fileName}'

    # with io.open(path,'rb') as file:
    #     content = file.read()
    content = file.read()

    #Store the response generated by the Vision AI
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #Iterate through the labels provided and find the dog breeds
    r = []
    for label in labels:
        breed = label.description
        result = wiki.search(breed)
        if(result != None):
            info = data.getInfo(result)
            info["breed"] = breed
            r.append(info)
    #print(r)
    return r