from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create-post'),
    path('add_post/', views.add_post, name='add-post')
]
