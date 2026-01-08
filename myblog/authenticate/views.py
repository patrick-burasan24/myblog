from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
def authenticate_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        username_error_message = process_username(username)
        password_error_message = process_password(password)

        if username_error_message == "" and password_error_message == "":
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return HttpResponseRedirect(reverse('blogs:index'))
            else:
                auth_error_message = "Authentication failed."
                return render(
                    request,
                    'login/login_form.html',
                    {
                        'username_error_message': username_error_message,
                        'password_error_message': password_error_message,
                        'auth_error_message': auth_error_message,
                    }
                )
        else:
            return render(
                request,
                'login/login_form.html',
                {
                    'username_error_message': username_error_message,
                    'password_error_message': password_error_message,
                }
            )
    return redirect('/login/')

def process_username(username):
    error_message = ""
    if len(username) < 1:
        error_message = "Username cannot be empty."
    elif len(username) > 50:
        error_message = "Username cannot exceed 50 characters."
    return error_message

def process_password(password):
    error_message = ""
    if len(password) < 1:
        error_message = "Password cannot be empty."
    elif len(password) > 50:
        error_message = "Password cannot exceed 50 characters."
    return error_message