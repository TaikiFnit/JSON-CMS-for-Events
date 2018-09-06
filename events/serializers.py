from rest_framework import serializers
from .models import User, Event, EventUser

#class EventSerializer(serializers.ModelSerializer):
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
#    description = serializers.TextField(required=False)
#    locale = serializers.CharField(max_length=255)
#    date = serializers.DateTimeField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'avatar_url', 'google_id', 'google_token')

class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ('is_presenter', 'slide_url')

class EventSerializer(serializers.ModelSerializer):
     users = UserSerializer(many=True)
     userevents = serializers.PrimaryKeyRelatedField(queryset=Event.eventuser_set.all())

     class Meta:
         model = Event
         fields = ('id', 'title', 'description', 'locale', 'date', 'users', 'eventusers')

