from django.shortcuts import render
from .forms import ReiwaForm
# Create your views here.

def index(request):
    return render(request, 'work06/index.html')

def top(request):
    return render(request, 'work06/top.html')

def reiwa(request):
    result = None
    if request.method == 'POST':
        form = ReiwaForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            result = 2018 + year
    else:
        form = ReiwaForm()
    return render(request, "work06/reiwa.html", {"form": form, "result": result})