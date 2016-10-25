from django.shortcuts import render
from .models import exercise
#from blog.views import post_list

# Create your views here.
def home_view(request):
	latihan = exercise.objects.all()
	context = {
		'latihan': latihan,
	}
	return render(request, 'portfolio/index.html', context)
