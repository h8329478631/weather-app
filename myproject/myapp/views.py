
# Create your views here.
import requests
from django.shortcuts import render



def home(request):
    city = request.GET.get('city', 'Satara')
    api_key = "e60acc4e9fc844febfb45512260504"

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"

    response = requests.get(url)
    data = response.json()

    weather = {
        "city": city,
        "temperature": data["current"]["temp_c"],
        "description": data["current"]["condition"]["text"],
        "icon": data["current"]["condition"]["icon"],
        "lat": data["location"]["lat"],
        "lon": data["location"]["lon"],

    }

    return render(request, "index.html", {"weather": weather})