from django.shortcuts import render
from .models import Albums
from django.http import Http404

# Create your views here.

def index(request):
    allAlbums = Albums.objects.all()
    return render(request, "app1/index.html", {'allAlbums':allAlbums})

def details(request, id):
    try:
        album = Albums.objects.get(id=id)
    except:
        raise Http404("Album doesn't exists")
    return render(request, "app1/details.html", {'album':album})