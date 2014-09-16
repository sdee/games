from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from inventory.models import Game
from django.http import HttpResponseRedirect

class GameForm(forms.Form):
  name = forms.CharField(max_length=100)

def index(request):
  games = Game.objects.all()
  context = {'games': games}
  return render(request, 'index.html', context)

def detail(request, game_id):
  response = "Game id: %s."
  return HttpResponse(response % game_id)

def new(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = GameForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            print "valid"
            g = Game(name=form.cleaned_data['name'])
            g.save()
            return HttpResponseRedirect('/game/'+str(g.id)) # Redirect after POST; change to details
    else:
        form = GameForm() # An unbound form

    return render(request, 'new.html', {
        'form': form,
    })
