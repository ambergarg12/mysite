from django.shortcuts import render
import requests
from googlesearch import search

# Create your views here.
def homepage(request):
    return render(request,'weather/Myfirstwebsite.html',{})
def weatherview(request):
    if request.method=='POST':
        city_name = request.POST['city']
        api_id = "88acad47482f3efd19552b641ac1e392"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_id}"
        response = requests.get(url)
        list_of_data = response.json()
        
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "name": str(list_of_data["name"]),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "icon": str(list_of_data['weather'][0]["icon"]),
            "description": str(list_of_data['weather'][0]["description"])
        }
        print(data)
    else:
        data={}
    return render(request,'weather/weather.html',data)
#88acad47482f3efd19552b641ac1e392
def spotify(request):
    if request.method=='POST':
        song_name = "spotify play"+request.POST['song']
        results = []
        for i in search(song_name,stop=1):
            print(i)
            results.append(i)
        # data for variable list_of_data
        songdata = {
            "song_id": str(results[0].split("/")[-1]),
            }
        print(songdata)
    else:
        songdata={}

    return render(request,'weather/spotify.html',songdata)