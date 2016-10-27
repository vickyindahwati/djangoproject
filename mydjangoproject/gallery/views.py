from django.shortcuts import render
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'gallery/index.html', context)