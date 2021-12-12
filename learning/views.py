from django.contrib import auth
from django.urls import resolve
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .constants import INSTITUTE_NAME


def home(request):
	return render(request, 'home.html', {'INSTITUTE_NAME': INSTITUTE_NAME})

def contact(request):
	return render(request, 'contact.html', {'INSTITUTE_NAME': INSTITUTE_NAME})

class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if (request.method == "GET"):
            return self.login_page(request, *args, **kwargs)
        elif (request.method == "POST"):
            return self.login(request, *args, **kwargs)

    def login(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_instructor:
                return redirect('professor_dashboard')
            elif user.is_learner:
                return redirect('learner_dashboard')
            else:
                return self.login_page(self, request, *args, **kwargs)
        else:
            messages.info(request, "Invalid Username or Password")
            return self.login_page(self, request, *args, **kwargs)

    def login_page(self, request, *args, **kwargs):
        return render(request, 'login.html', {'INSTITUTE_NAME': INSTITUTE_NAME})
