from rest_framework import serializers

from .models import Group, Message


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','uuid', 'chatname', 'members']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','author', 'timestamp', 'content', 'group']
