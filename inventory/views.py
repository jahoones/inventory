from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

def index (request):
    return HttpResponse("Inventory webs")


