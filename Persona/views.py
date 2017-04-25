from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def persona(request,id):
    return HttpResponse("<html><head><body><p>la informacion de la persona %s</p><a href=\"/logout/\">Logout</a></body></head></html>" %id)