from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django import forms
from .forms import SearchForm
import pykemon

from .models import Pokemon


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if(form.is_valid()):
            return HttpResponseRedirect('/')
        
    else:
        form = SearchForm()
        
    return render(request, 'pokepy/index.html', {'form': form})
    
# def search(request):
#     query = Search(query)
#     query.query_text = request
#     template = loader.get_template('pokepy/search_results.html')
#     context = RequestContext(query, {
#         'query': query,
#     })
#     return HttpResponse(template.render(context))


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if(form.is_valid()):
            r = form.cleaned_data['search_query']
#             r="pikachu"
            if r.isalpha(): 
                a = "string." 
            else: 
                a= "an error, obviously"
            print('r=' + r + "\nr is a " + a) 
            poke=pykemon.get(pokemon=r)
            
    else:
        if 'request.poke' not in locals():
            return HttpResponseRedirect('/')
    
    template = loader.get_template('pokepy/search.html')
    move = list(poke.moves.keys())[0]
    egg_group = list(poke.egg_groups.keys())[0]
    context = RequestContext(request, {
        'poke': poke,'move': move,'egg_group': egg_group,
    })
    return HttpResponse(template.render(context))
    
#     poke = pykemon.get(pokemon=request.name)
#     move = list(poke.moves.keys())[0]
#     egg_group = list(poke.egg_groups.keys())[0]
#     template = loader.get_template('pokepy/search_result.html')
#     context = RequestContext(request, {
#         'poke': poke,'move': move,'egg_group': egg_group,
#     })
#     return HttpResponse(template.render(context))
    