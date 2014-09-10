from django.db import models

class Genre(models.Model):
  name = models.CharField(max_length=200)

# Create your models here.
class Game(models.Model):
    LOCATION = (
      ('H', 'Home'),
      ('W', 'Work'),
      ('C', 'Car'),
      ('S', 'Sell'),
    )
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=1, choices=LOCATION, default='H')
    genres = models.ManyToManyField(Genre)
    comment = models.CharField(max_length=500, default='')
