from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {
        "title": "Головна сторінка"
    }
    return render(request, "employees/index.html", data)