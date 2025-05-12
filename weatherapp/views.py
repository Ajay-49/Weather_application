from django.shortcuts import render
import requests

def compare_weather(request):
    city1 =request.GET.get('city1')
    city2 =request.GET.get('city2')
    saved_cities =request.session.get('saved_cities', []) 
    if 'save_city' in request.GET:
        city_to_save_source =request.GET['save_city']
        city_to_save = request.GET.get(city_to_save_source)
        if city_to_save and city_to_save not in saved_cities:
            saved_cities.append(city_to_save)
            request.session['saved_cities'] = saved_cities
    data = {}
    if city1 and city2:
        api_key = '61a1d5894de6d6ee4a35558770b1f947'
        url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
        res1 =requests.get(url.format(city1, api_key)).json()
        res2 =requests.get(url.format(city2, api_key)).json()
        data = {
             'city1': {
                'name': res1.get('name'),
                'temp':res1.get('main',  {}).get('temp'),
                'humidity': res1.get('main', {}).get(' humidity'),
                'desc': res1.get('weather', [{}])[0].get('description'),
            },
               'city2': {
                'name':res2.get('name'),
                'temp':res2.get('main', {}).get('temp'),
                'humidity': res2.get('main', {}).get('humidity'),
                'desc': res2. get('weather', [{}])[0].get('description'),
            }
        }
    return render(request, 'index.html', {'data': data, 'saved_cities': saved_cities})




















