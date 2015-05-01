from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the internet! Suck my cock!")
    
def admin(request):
    return HttpResponse("Hello, world. You're the admin.")
    
def search(request):
    return HttpResponse("Hello, consumer. You are the the search.")