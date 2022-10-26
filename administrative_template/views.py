from multiprocessing import context
from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    context = {'message' : 'Oi'}
    return render(request, 'administrative_template/starter.html', context)

def cards(request):
    r =requests.get('https://randomuser.me/api/')
    user = json.loads(r.text)["results"][0]    
    context = {
        "name": user["name"]["first"] + " " + user["name"]["last"],
        "city": user["location"]["city"],
        "country": user["location"]["country"],
        "email": user["email"],
        "age": user["dob"]["age"],
        "cell": user["cell"],
        "image": user["picture"]["large"]
    }
    return render(request, 'administrative_template/cards.html', context)