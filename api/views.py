# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from django.core.cache import cache
# Create your views here.




def mater(request):
    query = request.GET.get("search")
    a = requests.get(
        f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{query}.TXT"
    )
    params = a.text.split()
    print(params)
    if cache.get(params[2]):
        print("Returning from cache")
        return JsonResponse(cache.get(params[2]))
    my_json = {
        "station": params[2],
        "last_observation": f"{params[0]} at {params[1]} GMT",
        "winds": f"The direction is {params[4][:3]} and the velocity {params[4][3:5]} knots",
        "temperature": params[7]
    }

    # Saving data in cache for 5 mints
    cache.set(params[2], my_json, 300)

    print("Returning from database")
    return JsonResponse(my_json)



def ping(request, slug):
    if slug  == "ping":
        return JsonResponse({"data":"pong"})
    else:
        return JsonResponse({"data":"No response"})