# -*- coding: utf-8 -*-
from google.cloud import vision
import json
import sys
import decimal

reload(sys)
sys.setdefaultencoding('utf-8')


def detect_properties_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    response = client.image_properties(image=image)
    temp = []
    props = response.image_properties_annotation
    for color in props.dominant_colors.colors:
        temp.append([{'fraction':str(color.pixel_fraction)},
           {'red':str(color.color.red)},
           {'green':str(color.color.green)},
           {'blue':str(color.color.blue)},
           {'alpha':str(color.color.alpha)}])
    temp.append({'url':uri})
    return temp



urls = []


file = open('five_5.json','a')
data = []
for i in urls:
    data.append(detect_properties_uri(i))
json.dump(data,file,ensure_ascii=False)
file.close()




