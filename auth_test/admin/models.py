from django.db import models
from mongoengine import *

class Users(Document):
    username = StringField(required=True)
    password = StringField(max_length=50)
    #first_name = StringField(max_length=50)
    #Userslast_name = StringField(max_length=50)



class Recipe(Document):
    name = StringField(required=True)
    ingredients = StringField(max_length=50)#ListField(StringField(max_length=30))
