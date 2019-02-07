from django.db import models

class Album(models.Model):
    title = models.CharField(max_length = 60)
    artist = models.CharField(max_length = 60)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()

class User(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)	
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()
