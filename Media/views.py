from django.shortcuts import render, redirect
from datetime import datetime as dt


# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_results(request):
    return render(request, 'search.html')