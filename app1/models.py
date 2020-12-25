from django.db import models

# Create your models here.

class Albums(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.artist+" "+self.album_title+" "+self.genre


class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)

    def __str__(self):
        return self.song_title