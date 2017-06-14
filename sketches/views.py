from django.http import HttpResponse
from django.template import loader
import os
import json
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
import pdb
from django.core.files.images import ImageFile#ContentFile
import cv2, numpy as np
import keras, base64

from models import *
template_dir = os.path.join(os.path.dirname(__file__),'templates')

def index(request):
    return HttpResponse( loader.get_template(os.path.join(template_dir,'index.html')).render({},request))

def download(request):
    with open('output.jpg', "rb") as f:
        return HttpResponse(base64.encodestring(f.read()), content_type="image/jpeg")
# @csrf_exempt
def convert(request):
    print request.FILES
    files =  request.FILES['pic']
    content= ImageFile(files.read())
    img = cv2.imdecode(np.fromstring(content.file, np.uint8), 0)
    print 'SHAPE',img.shape
    cv2.imwrite('input.jpg',img)
    img = cv2.imread('input.jpg',0)
    
    gen = img2img(img)
    cv2.imwrite('output.jpg',gen)#1
    
    # pprint (dir(request))
    # pdb.set_trace() 
    # print request.params
    return HttpResponse( "hi")
    # response_data = {"type":"text","message": msg if len(msg)>0 else 'Hi'}
    # output = answer(msg)
    # print output
    # if output['status'] == 'OK':
        # return HttpResponse(json.dumps(output), content_type="application/json")
    # else:
        # return HttpResponse(json.dumps(output['msg']),status=500,content_type="application/json")