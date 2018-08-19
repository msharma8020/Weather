import requests
from django.shortcuts import render
from .models import Weather
from .forms import CityForm

# Create your views here.

def index(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=13aaa8fec6c229e8e3c414b1ebfdde1e"

    if(request.POST):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    city_data = []

    cities = Weather.objects.all()

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
        "city" : city,
        "temperature" : r["main"]["temp"],
        "description" : r["weather"][0]["description"],
        "icon" : r["weather"][0]["icon"]
        }

        city_data.append(city_weather)

    context = { "city_data" : city_data ,"form" : form}

    return render(request, "weather/weather.html",context)

