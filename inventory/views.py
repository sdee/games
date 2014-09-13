from django.shortcuts import render

# Create your views here.
from inventory.models import Game

def index(request):
  games = Game.objects.all()
  context = {'games': games}
  return render(request, 'index.html', context)
