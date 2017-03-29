from django.shortcuts import render
from django.http import HttpResponse
from mongoengine.django.auth import *
from .models import Users
from django.contrib.auth import authenticate, login, logout
from mongoengine.queryset import DoesNotExist
from mongoengine import *


from .models import *
# Create your views here.
def new_user(request):
    print("In new_user")
    if request.method == "POST":
        user = User.create_user(request.POST['your_name'], request.POST['pwd'])
        user.save()
        return render(request, "new_user.html")
    else:
        return render(request, "new_user.html")

def index(request):
    print("Im in index")
    if request.method == "POST":
        username = request.POST['your_name']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)

        if user is not None:
            user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            try:
                request.session['user'] = user
                login(request, user)
            except User.DoesNotExist:
                print("error does not exist")
            if user.is_authenticated:
                return render(request, "loggedin.html")
        else:
            return HttpResponse('login failed')
    else:
        return render(request, "admin_loggin.html")