from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    color = models.CharField(max_length=20, default='red')
    email = models.EmailField(max_length=50, blank=True)
    flavor = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Renote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    retitle = models.CharField(max_length=200)
    recontent = models.TextField(default='Renote default message')

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
