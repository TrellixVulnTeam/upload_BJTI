from mongoengine import *
import mongoengine
import datetime
from django.db import models

# Create your models here.
class users(Document):
    _id = StringField()
    user_name = StringField(required=True)
    password = StringField(required=True)
    is_staff = mongoengine.BooleanField(default=False, required=True)
    #kanske ta bort mongoengine samt requeerd
    is_superuser = mongoengine.BooleanField(default=False, required=True)
    last_login = DateTimeField(default = datetime.datetime.now)

class user(Document):
    _id = StringField()
    username= StringField(required=True)
    password = StringField(required=True)



