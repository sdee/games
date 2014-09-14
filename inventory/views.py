from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from inventory.models import Game

def index(request):
  games = Game.objects.all()
  context = {'games': games}
  return render(request, 'index.html', context)

def detail(request, game_id):
  response = "Game id: %s."
  return HttpResponse(response % game_id)
