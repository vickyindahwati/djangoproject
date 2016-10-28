from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	form = PostForm()
	context = {
		"form": form,
	}
	return render(request, "blog/post_form.html", context)

def post_detail(request, id=None):
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "blog/post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset, 
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