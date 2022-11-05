from django.http import JsonResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def Artiste_list(request):
    if request.method == 'GET':
        Artiste = Artiste.object.all()
        serializer = ArtisteSerializer(Artiste, many = True)
        return JsonResponse({'Artiste': serializer.data})

    if request.method == 'POST':
        serializer = ArtisteSerializer(data=request.date)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Artiste_detail(request, id):

    try:
        Artiste = Artiste.objects.get(pk=id)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer=ArtisteSerializer(Artiste)
       return Response(serializer.data)

    elif request.method == 'PUT':
       serializer = ArtisteSerializer(Artiste, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 