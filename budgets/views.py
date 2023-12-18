from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from budgets.forms import BudgetCreationForm
from budgets.models import Budget
from finances.models import FinanceOperation


class BudgetController(View):
    '''Регистрация'''

    template_name = 'budgets/create_budget.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        form = BudgetCreationForm()
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)

    def post(self, request):
        '''Пользователь уже ввел данные и отправил форму'''
        form = BudgetCreationForm(request.POST)

        if form.is_valid():
            Budget.objects.create(
                goal=form.cleaned_data['goal'],
                address=form.cleaned_data['address'],
                status=form.cleaned_data['status'],
            )
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)


def delete_budget(request, pk):
    item = Budget.objects.get(pk=pk)
    item.delete()
    return redirect(reverse('list_budgets'))


class BudgetListController(View):
    '''Регистрация'''

    template_name = 'budgets/list_budgets.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        items = Budget.objects.all()
        context = {"items": items}
        return render(request=request, template_name=self.template_name, context=context)
