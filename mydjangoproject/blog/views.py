from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	context = {
		"title": "Detail"
	}
	return render(request, "blog/index.html", context)

def post_list(request):
	context = {
		"title": "List"
	}
	return render(request, "blog/index.html", context)

def post_update(request):
	context = {
		"title": "Update"
	}
	return render(request, "blog/index.html", context)

def post_delete(request):
	context = {
		"title": "Delete"
	}
	return render(request, "blog/index.html", context)