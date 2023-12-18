from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View
from django.contrib.auth import logout, login

from users.forms import UserModelCreationForm
from users.services.registration import RegistrationService


@method_decorator(login_required, name="get")
class LogoutUserView(View):
    '''Выход из системы'''

    def get(self, request):
        logout(request)
        return redirect(reverse('list_budgets'))


class RegistrationController(View):
    '''Регистрация'''

    template_name = 'registration/registration.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        form = UserModelCreationForm()
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)

    def post(self, request):
        '''Пользователь уже ввел данные и отправил форму'''
        form = UserModelCreationForm(request.POST)

        if form.is_valid():
            user = RegistrationService.register(form.cleaned_data)
            login(request, user)
            return redirect(reverse('list_operations'))
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)
