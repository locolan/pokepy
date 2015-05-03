from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.conf import settings
from django.db import models
from django import forms
from .forms import SearchForm
from importlib import import_module
import pykemon,simplejson
from pykemon import api,request,models
import re

from .models import Pokemon, Moves, Abilities


def valid_address(request,form):
    poke = request.session.get('pokename')
    if(form.is_valid()):
        r = form.cleaned_data['search_query'] 
        print("search_query: " + r)
        try:
            poke = pykemon.get(pokemon=r)
            print("poke.name" + poke.name)
            
#             try:

            p = Pokemon(name=poke.name, id=poke.id,
                        description=poke.descriptions, egg_group=poke.egg_groups,)
            
            i = 0
            kv=""
            
#             for key, value, kwargs in poke.types:
#                 i = i + 1
#                 kv = key
#                 if(i==1):
#                     t1 = kv
#                 if(i==2):
#                     t2 = kv
                    
#             p.add(type1=t1)
#             p.add(type2=t2)
            
            #p.commit()
            p.save()
            m = poke.moves
            a = poke.abilities
            for f in m:
                butt = Moves.objects.create(move=f)
                butt.save()
                
                
            for f in a:
                ding = Abilities.objects.create(ability=f)
                ding.save()
                
            
            
#             print(butt + " " + dong) 
            
            
            print("Here")
            print(p.name + " A " + p.type1 + " Pokemon!")
#             except: # KeyError:
#                 pass
            
#             print(poke.name + " conversion to JSON")
#             
#             mylist = list(poke.get_queryset().values_list('code', flat=True))
#             print("mark 1")
#             json_data = json.dumps(mylist)
#             print("mark 2")
#             response = HttpResponse(json_data, content_type='application/json')
#             print("mark 3")
            request.session['pokename'] = poke.name
            print("poke.name: " + poke.name)
            print("session pokename: " + request.session.get('pokename') )
            
        except(pykemon.ResourceNotFoundError):
            print("Why does this keep happening?")

        print("True")
        return True
    
    print("False outer")
    return False


def meth_is_POST(request,form):
    if request.method == 'POST':
        print("form")
        foo = valid_address(request,form)    
        if  foo == False:
#             move = ""
#             egg_group = ""
#             form = SearchForm()
#             context = RequestContext(request, { 'move': move,
#                                            'egg_group': egg_group,'form': form,
#                                            })
#             
#             return context
            return True
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
    n = request.session.get('pokename')
    p = Pokemon.objects.get(name__contains=n)
    print("p: " + p.name )
    try:
        #move = list(p.moves.keys())[0]
        #egg_group = list(p.egg_groups.keys())[0]
        form = SearchForm()
        r = re.compile(r"([\w]+_gen_5",)
        description = p.description[]
        print("am i even")
        context = RequestContext(request, {'name':p.name, 'description':description,    
            'form': form,
        })
        
        print(context)
        return HttpResponse(template.render(context))
        
    except AttributeError:
        return HttpResponseRedirect('/')
    
    
    