from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list_products(request):
    html = "<p>Ürünler</p>"
    return HttpResponse(html)
