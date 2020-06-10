# -*- coding: utf-8 -*-
import json
import sys
 
reload(sys)
sys.setdefaultencoding('utf-8')
def detect_labels_uri(uri):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    response = client.label_detection(image=image)
    labels = response.label_annotations
    #print('Labels:')
    temp = []
    for label in labels:
        temp.append([{'label':label.description},{'score':label.score},{'topicality':label.topicality}])
    temp.append({'url':uri})
    return temp

urls = []



file = open('Five.json','a')
data = []
for i in urls:
    data.append(detect_labels_uri(i))
json.dump(data,file,ensure_ascii=False)
file.close()
