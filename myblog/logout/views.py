from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def logout_from_application(request):
    if request.user.is_authenticated:
        logout(request=request)
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect(reverse('blogs:index'))
