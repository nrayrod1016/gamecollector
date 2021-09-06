from django.shortcuts import render, redirect
from .models import Game, Toy 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PlayingForm 
# Create your views here.





# Define the home view 
def home(request): 
  return render(request, 'home.html')

def about(request): 
  return render(request, 'about.html')

def games_index(request): 
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id): 
  game = Game.objects.get(id=game_id)
  playing_form = PlayingForm() 
  return render(request, 'games/detail.html', { 'game': game, 'playing_form': playing_form} )
 
def add_playing(request, game_id):
  form = PlayingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_playing = form.save(commit=False)
    new_playing.game_id = game_id
    new_playing.save()
  return redirect('games_detail', game_id=game_id)

class GameCreate(CreateView): 
  model = Game 
  fields = "['title', 'gameType', 'system', 'age']"
  success_url = '/games/'


class GameUpdate(UpdateView):
  model = Game 
  fields = ['name', 'gameType', 'system', 'year']


class GameDelete(DeleteView): 
  model = Game
  success_url = '/games/' 



class ToyCreate(CreateView): 
  model = Toy 
  fields = '__all__'

class ToyList(ListView): 
  model = Toy 
  

class ToyDetail(DetailView): 
  model = Toy 


class ToyUpdate(UpdateView): 
  model = Toy 
  fields = ['name', 'color']


class ToyDelete(DeleteView): 
  model = Toy 
  success_url = '/toys/'