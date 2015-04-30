from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")
    
def admin(request):
    return HttpResponse("Hello, world. You're at the admin.")
    
def search(request):
    return HttpResponse("Hello, world. You're at the search.")