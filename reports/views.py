from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from finances.forms import FinanceOperationCreationForm
from finances.models import FinanceOperation
from reports.forms import ReportCreationForm
from reports.models import Report


class ReportController(View):

    template_name = 'reports/create_report.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        form = ReportCreationForm()
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ReportCreationForm(request.POST)

        if form.is_valid():
            Report.objects.create(report_amount=form.cleaned_data["report_amount"],
                                  report_type=form.cleaned_data["report_type"],
                                  description=form.cleaned_data["description"])
        context = {'form': form, 'is_admin': True}
        return render(request, self.template_name, context)


def delete_report(request, pk):
    item = Report.objects.get(pk=pk)
    item.delete()
    return redirect(reverse('list_reports'))


class ReportListController(View):
    '''Регистрация'''

    template_name = 'reports/list_reports.html'

    def get(self, request):
        '''Если пользователь только зашел на страницу, просто отображаем форму'''
        items = Report.objects.all()
        context = {"items": items}
        return render(request=request, template_name=self.template_name, context=context)
