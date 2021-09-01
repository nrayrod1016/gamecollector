from django.db import models
from django.urls import reverse 
from datetime import date


PLAY = ( 
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

# Create your models here.
class Game(models.Model): 
  name = models.CharField(max_length=100)
  gameType = models.CharField(max_length=100)
  system = models.CharField(max_length=100)
  year = models.IntegerField()



  def __str__(self): 
    return self.name 

  def get_absolute_url(self):
    return reverse('games_detail', kwargs={'game_id': self.id})


class Playing(models.Model): 
  date = models.DateField('Playing Date') 
  meal = models.CharField(
    max_length=1, 
    choices=PLAY, 
    default=PLAY[0][0]
    )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self): 
    return f"{self.get_play_display()} on {self.date}" 

  class Meta:
    ordering = ['-date']