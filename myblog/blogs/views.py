from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Post


# Create your views here.
@login_required
def index(request):
    # Return the latest 10 blog posts
    blog_posts = Post.objects.order_by('-date').all()[:10]
    return render(
        request,
        'blogs/index.html',
        {'blog_posts': blog_posts}
    )

@login_required
def create_post(request):
    return render(request, 'blogs/create_post.html')

@login_required
def add_post(request):
    if request.method == 'POST':
        print('I got accessed!')
        post_title = request.POST.get('post-title')
        post_text = request.POST.get('post-text')

        post_title_error_message = process_post_title(post_title)
        post_text_error_message = process_post_text(post_text)

        if post_title_error_message == '' and post_text_error_message == '':
            Post.objects.create(
                title=post_title,
                content=post_text,
                author=request.user.username,
                date=datetime.now(),
                excerpt=post_text[:50],
            )
            return HttpResponseRedirect(reverse('blogs:index'))
        else:
            return render(
                request,
                'blogs/create_post.html',
                {
                    'post_title_error_message': post_title_error_message,
                    'post_text_error_message': post_text_error_message
                }
            )
    return redirect('blogs:create_post')

def process_post_title(post_title):
    error_message = ''
    if len(post_title) < 1:
        error_message = 'Post title cannot be empty.'
    elif len(post_title) > 50:
        error_message = 'Post title cannot exceed 50 characters.'
    return error_message

def process_post_text(post_text):
    error_message = ''
    if len(post_text) < 1:
        error_message = 'Post must have content before it may be published.'
    elif len(post_text) > 5000:
        error_message = 'Posts cannot exceed 5000 characters.'
    return error_message