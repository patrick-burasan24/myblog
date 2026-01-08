from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post


# Create your views here.
def index(request):
    # Check if user is admin
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    # Return the latest 10 blog posts
    blog_posts = Post.objects.order_by('-date').all()[:10]
    return render(
        request,
        'blogs/index.html',
        {'blog_posts': blog_posts}
    )


def create_post(request):
    pass
