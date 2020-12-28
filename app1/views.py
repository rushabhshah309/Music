from django.shortcuts import render, get_object_or_404
from .models import Albums, Song
#from django.http import Http404

# Create your views here.

def index(request):
    allAlbums = Albums.objects.all()
    return render(request, "app1/index.html", {'allAlbums':allAlbums})

def details(request, id):
    #album = Albums.objects.get(id=id)
    album = get_object_or_404(Albums, id=id)
    return render(request, "app1/details.html", {'album':album})

def favorite(request, id):
    album = get_object_or_404(Albums, id=id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, "app1/details.html", {"album":album, "error_message":"you didn't selected any song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, "app1/details.html", {'album':album})