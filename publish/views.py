from django.shortcuts import render

# Create your views here.


from django.http import Http404
from django.shortcuts import render
from .models import Post


# Windows   celery -A quick_publisher worker --pool=solo -l info
#  Periodic tasks  celery -A quick_publisher beat
'''
Download Redis-x64-2.8.2104.zip
Extract the zip to prepared directory

run redis-server.exe
'''


def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")

    post.view_count += 1
    post.save()

    return render(request, 'publish.html', context={'post': post})