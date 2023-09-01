from django.shortcuts import render

from .models import Post
# Create your views here.


def posts(request):
    images = Post.objects.all()
    return render(request, 'gallery/index.html', {'images': images})
