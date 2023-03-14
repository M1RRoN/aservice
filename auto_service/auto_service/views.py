from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render


def index(request):
    return render(request, 'auto_service/index.html')

class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login'
    success_message = 'Вы залогинены'
    success_url = 'auto_service/index'


class LogoutUser(SuccessMessageMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().get(request, *args, **kwargs)
