from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from chat.models import Room, Message, CsvUpload
from .serializers import RoomSerializer, MessageSerializer, CsvUploadSerializer
from django.http import HttpResponseRedirect
from chat import dowellconnection
import json

@api_view(['GET',])
def room_list(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(('GET',))
def getMessages(request, room):
    serializer = MessageSerializer
    if request.method == 'GET':
#        usr = request.session.get("user_name")
        room_name = Room.objects.get(name=room)
        messages = Message.objects.filter(room=room_name.id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#       ********
    '''
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''

@api_view(('POST',))
def sendMssg(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    else:
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






    # for sendMssg
    '''
    sssionUser = request.session.get("user_name")
#    sssionItem = request.session.items()
    if sssionUser:
        serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
