from django.http import HttpResponse

def top(request):
    return HttpResponse("Work05 top page")

def index(request):
    return HttpResponse("Work05 index page")

def list(request):
    return HttpResponse("Work05 list page")
