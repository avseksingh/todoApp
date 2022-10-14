from django.shortcuts import render
from django.http import HttpResponse
from . import models
from datetime import datetime
from .models import Todo
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def add(request):
    title, description, lastModified,submit, add, modify, delete = "", "", "", "", "", "", ""
    if request.GET:
        add = request.GET['add']
        modify = request.GET['modify']
        delete = request.GET['delete']

        title = request.GET['title']
        description = request.GET['description']
        now = datetime.now()
        lastModified = now.strftime("%H:%M:%S")
        store = Todo(title = title, description = description, last_modified = lastModified)
        store.save()
        updated = Todo.objects.all()
        return render(request, "add.html", {'title':title, 'description':description, 'lastModified':lastModified,"updated": updated})
    return render(request, "add.html")







