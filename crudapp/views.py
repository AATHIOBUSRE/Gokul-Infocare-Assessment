from django.shortcuts import render
from rest_framework import decorators,request,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import CrudModels
from .serializers import CrudSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@api_view(['GET','POST'])
def getcontact(request):
    if request.method == 'GET':
        contact = CrudModels.objects.all()
        serialzer = CrudSerializer(contact,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialzer = CrudSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_200_OK)
        else:
            return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def updatec(request,pk):
    try:
        contact = CrudModels.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CrudSerializer(contact)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CrudSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
def home(request):
    return render(request, "index.html")
