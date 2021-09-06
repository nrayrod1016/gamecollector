from django.db import models
from django.db.models.deletion import CASCADE 
from django.urls import reverse 
from datetime import date


PLAY = ( 
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

# Create your models here.

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Game(models.Model): 
  name = models.CharField(max_length=100)
  gameType = models.CharField(max_length=100)
  system = models.CharField(max_length=100)
  year = models.IntegerField()
  toys = models.ManyToManyField(Toy)


  def __str__(self): 
    return self.name 

  def get_absolute_url(self):
    return reverse('games_detail', kwargs={'game_id': self.id})

  def play_for_today(self): 
    return self.playing_set.filter(date=date.today()).count() >= len(PLAY)


class Playing(models.Model): 
  date = models.DateField('Playing Date') 
  play = models.CharField(
    max_length=1, 
    choices=PLAY, 
    default=PLAY[0][0]
    )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self): 
    return f"{self.get_play_display()} on {self.date}" 

  class Meta:
    ordering = ['-date']


