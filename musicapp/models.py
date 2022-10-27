from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.CharField(max_length= 40)
    likes = models.CharField(max_length= 40)
    artiste_id = models.CharField(max_length= 40)

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    song_id = models.CharField(max_length= 400)
