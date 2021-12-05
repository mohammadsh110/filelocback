import json
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from shutil import copyfile

global filePath
defaultPath = "https://185.208.175.202/public_html/Store/";



# Create your views here.
def createFilePath(f):
    lat = f['lat']
    lon = f['lon']
    response = requests.get(
        f'https://us1.locationiq.com/v1/reverse.php?key=pk.62eda30fdbc22fb0c627dbb2766edfca&lat={lat}&lon={lon}&format=json')
    geodata = response.json()
    path = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
    filePath = defaultPath + str(geodata.get('address').get('city')) + "/"
    try:
        if not os.path.isdir(filePath):
            os.mkdir(filePath)
        os.system(f'chmod 777 -R {filePath}')
        tempfilePath.split('/')[-1]
        copyfile(tempfilePath, filePath + tempfilePath.split('/')[-1])
    except:
        pass

def handle_uploaded_file_image(f):
    try:
        f = f['file']

        # path = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        # new_path = '/home/saam/Documents/shammasi/upload/' + 'temp' + "/"
        # try:
        #     os.mkdir(new_path)
        # except:
        #     pass
        global tempfilePath
        tempfilePath = defaultPath + str(f.name)
        with open(tempfilePath, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

            os.system(f'chmod 777 -R {tempfilePath}')
            return "True"
    except Exception as e:
        return str(e)


@csrf_exempt
def location(request):
    if request.method == 'POST':
        if request.POST:
            createFilePath(request.POST)
    return HttpResponse(json.dumps('result'), content_type='application.json')


@csrf_exempt
def uploadImage(request):
    if request.method == 'POST':
        if request.FILES:
            result = handle_uploaded_file_image(request.FILES)
        return HttpResponse(json.dumps(result), content_type='application.json')

    else:
        result = {
            "status": "Not Get Method Allowed",
        }
        return HttpResponse(json.dumps(result), content_type='application.json')
