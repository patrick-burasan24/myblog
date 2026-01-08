from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def login_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/blogs')
    return render(
        request,
        'login/login_form.html'
    )
