import json
import sys
from google.cloud import vision

reload(sys)
sys.setdefaultencoding('utf-8')
def detect_faces_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    response = client.face_detection(image=image)
    faces = response.face_annotations
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
    #print('Faces:')
    temp = []
    for face in faces:
        temp.append(['anger:{}'.format(likelihood_name[face.anger_likelihood]),
            'joy: {}'.format(likelihood_name[face.joy_likelihood]),
            'surprise: {}'.format(likelihood_name[face.surprise_likelihood])])
        vertices = (['({},{})'.format(vertex.x, vertex.y) 
            for vertex in face.bounding_poly.vertices])
        temp.append(['face bounds: {}'.format(','.join(vertices))])
    temp.append({'url':uri})
    return temp


urls = []



file = open('five.json','a')
data=[]
for i in urls:
    data.append(detect_faces_uri(i))

json.dump(data,file,ensure_ascii = False)
file.close()
