from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/create-post', views.create_post, name='create-post'),
]
