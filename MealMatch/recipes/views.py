from django.shortcuts import render
from mongoengine import *
from django.http import HttpResponse
from recipes.models import *

# Create your views here.
def startpage(request):
    #recipes = Recipe.objects()
    #print(recipes)
    #namn = ""
    #for name in recipe.objects:
     #   namn = namn + " " + name.rating[0]

    recipes = recipe.objects.get()




    return HttpResponse(recipes.payload["ingredients"][0]["amount"])
