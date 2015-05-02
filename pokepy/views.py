from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.conf import settings
from django import forms
from .forms import SearchForm
from importlib import import_module
import pykemon,simplejson
from pykemon import api,request,models

from .models import Pokemon


def poke_to_json(poke):
    return simplejson.JSONEncoder(poke)
    


def valid_address(request,form):
    poke = request.session.get('poke')
    if(form.is_valid()):
        r = form.cleaned_data['search_query'] 
        print(r)
        try:
            poke = pykemon.get(pokemon=r)
            poke_moves = []
            poke_abils = []
            for f in poke.moves:
                poke_moves.append(f)
            for f in poke.abilities:
                poke_abils.append(f)
            try:
                p = Pokemon(name=poke.name,
                            type1 = poke.types.popitem(), type2 = poke.types.popitem(),
                            games=poke.games, description=poke.description,
                            egg_group=poke.egg_groups, moves=poke_moves,
                            abilities=poke_abils,
                            )
                p.save()
            except KeyError:
                pass
            
#             print(poke.name + " conversion to JSON")
#             
#             mylist = list(poke.get_queryset().values_list('code', flat=True))
#             print("mark 1")
#             json_data = json.dumps(mylist)
#             print("mark 2")
#             response = HttpResponse(json_data, content_type='application/json')
#             print("mark 3")
            request.session['poke'] = poke.id
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
    request.session['poke'] = 0
    poke = "" 
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
        
        
        
#         print(poke.name + " conversion to JSON")
#         
#         mylist = list(poke.get_queryset().values_list('code', flat=True))
#         print("mark 1")
#         json_data = json.dumps(mylist)
#         print("mark 2")
#         response = HttpResponse(json_data, content_type='application/json')
#         print("mark 3")
#         print("compiling context")
        
        
        context = RequestContext(request, {
            'move': move,'egg_group': egg_group,
            'form': form,'poke': poke,
        })
        
        print("END")
        
        return HttpResponse(template.render(context))
        
    except AttributeError:
        return HttpResponseRedirect('/')
    
    
    