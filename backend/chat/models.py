from django.db import models
from django_resized import ResizedImageField


class CustomUser(models.Model):
    username = models.CharField(max_length=255, blank=False)

    class Meta():
        username = ['username']


class Room(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = ResizedImageField(force_format='WEBP', size=None,scale=0.5, quality=75, upload_to='images', blank=True, null=True)


    class Meta:
        room_name = ['name']


class Message(models.Model):
    message_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    class Meta:
        message_created = ['created_at']
