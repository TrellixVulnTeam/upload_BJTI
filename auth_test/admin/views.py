from django.shortcuts import render
from django.http import HttpResponse
from mongoengine.django.auth import *
from .models import Users
from django.contrib.auth import authenticate, login
from mongoengine.queryset import DoesNotExist
from mongoengine import *


from .models import *
# Create your views here.
#def index(request):
 #   if request.method == "POST":
  #      user = User.create_user(request.POST['your_name'], request.POST['pwd'])
   #     user.save()
    #    return render(request, "admin_loggin.html")
    #else:
     #   return render(request, "admin_loggin.html")

def index(request):
    if request.method == "POST":
        username = request.POST['your_name']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)


        print(user)
        print("heeeej")
        if user is not None:
            user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            try:
                request.session['user'] = user
                login(request, user)
            except User.DoesNotExist:
                print("sjukt oklart")
            #request.session['user'] = user
            if user.is_authenticated:
                return render(request, "loggedin.html")
        else:
            return HttpResponse('login failed')
    else:
        return render(request, "admin_loggin.html")