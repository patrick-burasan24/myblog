from django.urls import path

from . import views

app_name = 'logout'
urlpatterns = [
    path('', views.logout_from_application, name='logout'),
]