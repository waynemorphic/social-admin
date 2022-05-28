from django.shortcuts import render, redirect
from datetime import datetime as dt


# Create your views here.
def index(request):
    return render(request, 'index.html')

# post for particular date
def post_of_day(request):
    date = dt.date.today()
    return render(request, {"date": date})

# getting the day of the week
def convert_dates(dates):
    # get weekday number for the particular date
    day_number = dt.date.weekday(dates)
    
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    # return the actual day
    day = days[day_number]
    return day

def search_results(request):
    return render(request, 'post/search.html')