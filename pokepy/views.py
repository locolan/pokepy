from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.conf import settings
from django import forms
from .forms import SearchForm
from importlib import import_module
import pykemon

from .models import Pokemon


def valid_address(request,form):
    poke = request.session.get('poke')
    if(form.is_valid()):
        r = form.cleaned_data['search_query'] 
        print(r)
        try:
            request.session['poke'] = pykemon.get(pokemon=r)
        except(pykemon.ResourceNotFoundError):
            print("Why does this keep happening?")
            pass
        print("True")
        return True
    print("False outer")
    return False


def meth_is_POST(request,form):
    if request.method == 'POST':    
        if valid_address(request,form) == False:
            move = ""
            egg_group = ""
            form = SearchForm()
            context = RequestContext(request, { 'move': move,
                                           'egg_group': egg_group,'form': form,
                                           })
            return context
        return True
    else:
        return False


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if(form.is_valid()):
            return HttpResponseRedirect('/')
        
    else:
        form = SearchForm()
        
    return render(request, 'pokepy/index.html', {'form': form})


def search(request): 
    request.session['poke'] = None
     
    form = SearchForm(request.POST)
    template = loader.get_template('pokepy/search.html')
    
    t = meth_is_POST(request, form)
    
    if t == True:
        print("True blue")
    elif t == False:
        return HttpResponseRedirect('/')
    else:    
        context = t
        return HttpResponse(template.render(context))
    
    try:
        poke = request.session.get('poke')
        print("poke")
        move = list(poke.moves.keys())[0]
        egg_group = list(poke.egg_groups.keys())[0]
        form = SearchForm()
        
        context = RequestContext(request, {
            'move': move,'egg_group': egg_group,
            'form': form,
        })
        print(poke.name + " , " + poke.weight)
        return HttpResponse(template.render(context))
        
    except AttributeError:
        return HttpResponseRedirect('/')
    
    
    