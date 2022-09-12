from rest_framework import serializers
from chat.models import Room, Message, CsvUpload
import json
#from .views import getMessages
#from django.http import HttpRequest

# To format json in MessageSerializer()
class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

class RoomSerializer(serializers.ModelSerializer):
#   name = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Room.objects.all())
    class Meta:
        model = Room
        fields = ['name']

class MessageSerializer(serializers.ModelSerializer):
    room_name = serializers.SerializerMethodField()
    def get_room_name(self, obj):
        roomiD = eval(obj.room)
        me = Object()
        me.name = Room.objects.all()[roomiD]
        if roomiD > 0:
            me.name = Room.objects.all()[roomiD-1]
            extJson = me.toJSON()
            getObjs = json.loads(extJson)
            roomName = getObjs['name']['name']
            return roomName
        if roomiD <= 0:
            me.name = Room.objects.all[0]
            extJson = me.toJSON()
            getObjs = json.loads(extJson)
            roomName = getObjs['name']['name']
            return roomName

    class Meta:
        model = Message
        fields = ['room', 'room_name', 'user', 'value', 'date']



class CsvUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvUpload
        fields = ['file_name', 'uploaded', 'activated']
