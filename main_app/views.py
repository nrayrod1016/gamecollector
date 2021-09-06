from django.shortcuts import render, redirect
from .models import Game, Toy 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView 
from .forms import PlayingForm 
# Create your views here.





# Define the home view 
class Home(LoginView): 
  template_name = 'home.html'

def about(request): 
  return render(request, 'about.html')

@login_required
def games_index(request): 
  # This reads ALL Games, not just logged in user's games 
  # games = Game.objects.all()
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id): 
  game = Game.objects.get(id=game_id)
  toys_game_doesnt_have = Toy.objects.exclude(id__in = game.toys.all().values_list('id'))
  playing_form = PlayingForm() 
  return render(request, 'games/detail.html', { 'game': game, 
  'playing_form': playing_form, 
  'toys': toys_game_doesnt_have} )
 
@login_required
def add_playing(request, game_id):
  form = PlayingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_playing = form.save(commit=False)
    new_playing.game_id = game_id
    new_playing.save()
  return redirect('games_detail', game_id=game_id)


class GameCreate(LoginRequiredMixin, CreateView): 
  model = Game 
  fields = ['name', 'gameType', 'system', 'year']
  success_url = '/games/'

  def form_valid(self, form): 
    form.instance.user = self.request.user 
    return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game 
  fields = ['name', 'gameType', 'system', 'year']


class GameDelete (LoginRequiredMixin, DeleteView): 
  model = Game
  success_url = '/games/' 



class ToyCreate(LoginRequiredMixin, CreateView): 
  model = Toy 
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView): 
  model = Toy 
  

class ToyDetail(LoginRequiredMixin, DetailView): 
  model = Toy 


class ToyUpdate(LoginRequiredMixin, UpdateView): 
  model = Toy 
  fields = ['name', 'color']


class ToyDelete(LoginRequiredMixin, DeleteView): 
  model = Toy 
  success_url = '/toys/'

@login_required
def assoc_toy(request, game_id, toy_id):
  Game.objects.get(id=game_id).toys.add(toy_id)
  return redirect('games_detail', game_id=game_id)


def signup(request): 
  error_message = ''
  if request.method == 'POST': 
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
      user = form.save() 
      login(request, user) 
      return redirect('games_index')
    else: 
      error_message = 'Invalid sign up - try again' 
  form = UserCreationForm() 
  context = {'form': form , 'error_message': error_message}
  return render(request, 'signup.html', context)

