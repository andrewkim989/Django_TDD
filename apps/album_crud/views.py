from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "answer": 42
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        Album.objects.create(title = request.POST["title"], 
        artist = request.POST["artist"], year = request.POST["year"])
    return redirect("/")

def edit(request, id):
    album = Album.objects.get(id = id)
    if request.method == "POST":
        album.title = request.POST["title"]
        album.artist = request.POST["artist"]
        album.year = request.POST["year"]
        album.save()
    return redirect("/")

def delete(request, id):
    #Album.objects.get(id = id)
    Album.objects.get(id = id).delete()
    return redirect("/")

def read(request, id):
    context = {
        "album": Album.objects.get(id = id)
    }
    return render(request, "index.html", context)

def newUser(request):
    if request.method == "POST":
        User.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], 
        email = request.POST["email"], password = request.POST["password"])
    return redirect("/")

def editUser(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.password = request.POST["password"]
        user.save()
    return redirect("/")

def deleteUser(request, id):
    User.objects.get(id = id).delete()
    return redirect("/")

def getUser(request, id):
    context = {
        "user": User.objects.get(id = id)
    }
    return render(request, "index.html", context)