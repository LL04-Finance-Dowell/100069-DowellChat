from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from chat.models import Room, Message, CsvUpload
from .serializers import RoomSerializer, MessageSerializer, CsvUploadSerializer
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse, HttpResponse
from chat import dowellconnection
import json
#import chatcollection
from .dowellpopulationfunction import targeted_population
import requests
import datetime

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


@api_view(('POST',))
def sendMssg(request):
#    if request.session.get("user_name"):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def getChats(request):
    resp = targeted_population('chat', 'chats', ['chat_details'], 'life_time')
    chats =[]
    for i in resp['normal']['data'][0]:
        chats.append(i['chat_details'])
    return JsonResponse({'chats':chats})

@csrf_exempt
def post(request):
    return render(request, 'ChatApi/test.html')

@csrf_exempt
def postChats(request):
    # Add Login Function Here and adjust the below code
    username = request.POST['username']
    room = request.POST['room']
    message = request.POST['message']

    def get_event_id():
        dd=datetime.datetime.now()
        time=dd.strftime("%d:%m:%Y,%H:%M:%S")
        url="https://100003.pythonanywhere.com/event_creation"
        data={
            "platformcode":"FB", "citycode":"101", "daycode":"0", "dbcode":"pfm", "ip_address":"192.168.0.41",
            "login_id":"lav", "session_id":"new", "processcode":"1", "regional_time":time, "dowell_time":time,
            "location":"22446576", "objectcode":"1", "instancecode":"100051","context":"afdafa ", "document_id":"3004",
            "rules":"some rules", "status":"work","data_type": "learn", "purpose_of_usage": "add",
            "colour":"color value", "hashtags":"hash tag alue", "mentions":"mentions value", "emojis":"emojis",
        }
        r=requests.post(url,json=data)
        return r.text
    url = "http://100002.pythonanywhere.com/"
    ddd=datetime.datetime.now()
    timeNow=ddd.strftime("%d:%m:%Y, %H:%M")

    payload = json.dumps({
        "cluster": "chat","database": "chat","collection": "chats","document": "chats",
        "team_member_ID": "10006902","function_ID": "ABCDE","command": "insert",
        "field": {
            "eventId":get_event_id(),
            "chat_details": {
                    "username": username,
                    "room": room,
                    "message": message,
                    "time": timeNow
                }
        },
        "update_field": {
            "order_nos": 21
        },
        "platform": "bangalore"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.request("POST", url, headers=headers, data=payload)
    output = res.text
    return JsonResponse({"New Message Created":output})


