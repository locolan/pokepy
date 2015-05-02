from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Pokemon


def index(request):
    pokemon_list = Pokemon.objects.order_by('name')[:5]
    template = loader.get_template('pokepy/index.html')
    context = RequestContext(request, {
        'pokemon_list': pokemon_list,
    })
    return HttpResponse(template.render(context))
    
def admin(request):
    return HttpResponse("Hello, world. You're the admin.")
    
def search(request):
    return HttpResponse("Hello, consumer. You are the the search.")