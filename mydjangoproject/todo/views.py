from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from todo.models import Schedule
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Schedule.objects.all()
    return render(request, 'todo/todo.html', {'posts': posts})

def post_remove(request, pk):
    post = get_object_or_404(Schedule, pk=pk)
    post.delete()
    return redirect('todo.views.post_list')


