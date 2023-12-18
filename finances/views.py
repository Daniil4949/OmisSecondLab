from django.shortcuts import render
from django.views import View

from finances.forms import FinanceOperationCreationForm
from finances.models import FinanceOperation


class FinanceOperationController(View):
    '''Регистрация'''

    template_name = 'finance_operations/create_operation.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        form = FinanceOperationCreationForm()
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)

    def post(self, request):
        '''Пользователь уже ввел данные и отправил форму'''
        form = FinanceOperationCreationForm(request.POST)

        if form.is_valid():
            FinanceOperation.objects.create(amount=form.cleaned_data["amount"],
                                            operation_type=form.cleaned_data["operation_type"],
                                            user=request.user)
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)


class FinanceOperationListController(View):
    '''Регистрация'''

    template_name = 'finance_operations/operation_list.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        items = FinanceOperation.objects.filter(user=request.user)
        context = {"items": items}
        return render(request=request, template_name=self.template_name, context=context)
