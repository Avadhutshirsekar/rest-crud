from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import  StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# #from .models import Student 
# # Create your views here.
# @csrf_exempt
# def student_create(request):
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    


# def student_api(request):
#     if request.method=='GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             stu=Student.objects
#             serializer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
        
#         stu=Student.object.all()
#         serializer=StudentSerializer(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
        


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'data is inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')











