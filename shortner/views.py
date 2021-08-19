from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url
import uuid

# Create your views here.

def home(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, unid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(unid=pk)
    ll =url_details.link
    return redirect(url_details.link)

