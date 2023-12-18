from django.contrib import admin
from django.urls import path, include
from .views import FinanceOperationController, FinanceOperationListController

## МАППИНГ УРЛОВ И КОНТРОЛЛЕРОВ
urlpatterns = [
    path('create_operation/', FinanceOperationController.as_view(), name='create_finance_operation'),
    path('list_operations/', FinanceOperationListController.as_view(), name='list_operations'),
]
