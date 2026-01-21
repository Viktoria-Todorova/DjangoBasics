from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from destinations.models import Destination


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('welcome to our travel application!')

def destinations_list(request: HttpRequest) -> HttpResponse:
    destinations = Destination.objects.all()
    context = {'destinations': destinations,
               'page_title': 'All Destinations',}

    return render(request, 'destination/list.html', context)


def destination_detail(request:HttpRequest,slug:str) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)
    context = {'destination': destination,
               'page_title': f'{destination.name} Details'}

    return render(request,'destination/detail.html',context)


def redirect_home(request:HttpRequest) -> HttpResponse:
    return redirect('destination:list') #temporary redirwct

def page_not_found(request, exception):
    return render(request, '404.html', status=404)