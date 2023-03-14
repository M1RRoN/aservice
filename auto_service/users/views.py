from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView

from users.forms import UserForm
from users.models import CustomUser


class RegisterUser(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно создан'



class UpdateUser(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = 'Пользователь обновлён'



class DeleteUser(SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = 'Пользователь удалён'
