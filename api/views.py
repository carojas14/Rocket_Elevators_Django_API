from datetime import datetime
from hashlib import new
from django.shortcuts import render
from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from datetime import datetime
from PIL import Image
import numpy as np
import face_recognition
import json


# Create your views here.
# https://python-reference.readthedocs.io/en/latest/docs/dunderattr/setattr.html

@api_view(['POST'])
def RegisterEmployee(request):
    image =face_recognition.load_image_file(request.data['photo'])
    unknown_face_encoding = face_recognition.face_encodings(image)[0]
    picture = list(unknown_face_encoding)
    pictureDump = json.dumps(picture)
    pictureJson = json.loads(pictureDump)
    new = Employees()
    data = {
        'firstName': request.data['firstName'],
        'lastName': request.data['lastName'],
        'title': request.data['title'],
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
        'keypoints': pictureJson
    }

    new.__setattr__('firstName', data['firstName'])
    new.__setattr__('lastName', data['lastName'])
    new.__setattr__('title', data['title'])
    new.__setattr__('updated_at', data['updated_at'])
    new.__setattr__('created_at', data['created_at'])
    new.__setattr__('keypoints', pictureJson)
    new.save()
    return Response(data)


# https://pythonguides.com/python-numpy-array/
# https://pythonguides.com/python-django-filter/


@api_view(['GET'])
def FacialRecognition(request):
    if(request.method == 'GET'):
        image = Image.open(request.data['image'])
        img_arr = np.array(image)
        unknown_face_encoding = face_recognition.face_encodings(img_arr)[0]

        queryset = Employees.objects.filter(keypoints = unknown_face_encoding.tolist())
        if queryset.exists():
            employee = queryset.first()
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        else:
            return Response("unidentified picture")



@api_view(['GET'])
def EmployeesList(request):
    if(request.method == 'GET'):
        try:
            employees = Employees.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(serializer.data, safe=False)
        except IndexError:
            quit()



