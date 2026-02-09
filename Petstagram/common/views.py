from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from photos.models import Photo


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets','like_set')

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html',context)