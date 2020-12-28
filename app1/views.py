from django.shortcuts import render, get_object_or_404
from .models import Albums
#from django.http import Http404

# Create your views here.

def index(request):
    allAlbums = Albums.objects.all()
    return render(request, "app1/index.html", {'allAlbums':allAlbums})

def details(request, id):
    #album = Albums.objects.get(id=id)
    album = get_object_or_404(Albums, id=id)
    return render(request, "app1/details.html", {'album':album})