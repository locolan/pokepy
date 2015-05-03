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

from .models import Pokemon, Moves, Abilities
from pykemon.exceptions import ResourceNotFoundError


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
            p.save()
            m = poke.moves
            a = poke.abilities
            for f in m:
                butt = Moves.objects.create(move=f)
                butt.save()
                
                
            for f in a:
                ding = Abilities.objects.create(ability=f)
                ding.save()
                
            
            
            print("Here")
            print(p.name + " a " + p.type1 + " Pokemon!")
            
            request.session['pokename'] = poke.name
            print("poke.name: " + poke.name)
            print("session pokename: " + request.session.get('pokename') )
            
        except(pykemon.ResourceNotFoundError):
            print("Why does this keep happening?") # INADEQUATE VALIDATION YOU FUCKER

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


def des_key_validate(des_key,x):
    print("des_key: " + des_key)
    print("x: " + x)
    try:
        d = pykemon.get(description_id=des_key)
    except ResourceNotFoundError:
        return False
    return d

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
    print('n: ' + n)
    p = Pokemon.objects.get(name__contains=n)
    print("p: " + p.name )
    try:
       
        print("p.name: " + p.name)
        x = p.name.lower()
        o = (x + "_gen_6")
        print("o: " + o)
        i=5
        des_key=""
        description=""
        gen = "_gen_"
        while(i>0):
            h = str(i)
            
            try:
                des_key = p.description.get( o )
                description = des_key_validate( des_key, x )
                if(description != False):
                    break
            except ResourceNotFoundError:
                i-=1
                print(i)
            o = (x + gen + h)
        
        print(des_key)
        
#         description = pykemon.get(description = des_key)
        print(description)
        print("am i even")
        context = RequestContext(request, {'name':p.name, 'description':description,    
            'form': form,
        })
        
        print(context)
        return HttpResponse(template.render(context))
        
    except AttributeError:
        return HttpResponseRedirect('/')
    
    
    