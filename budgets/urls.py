from django.contrib import admin
from django.urls import path, include
from .views import BudgetController, BudgetListController, delete_budget

## МАППИНГ УРЛОВ И КОНТРОЛЛЕРОВ
urlpatterns = [
    path('create_budget/', BudgetController.as_view(), name='create_budget'),
    path('delete_budget/<int:pk>/', delete_budget, name='delete_budget'),
    path('list_budgets/', BudgetListController.as_view(), name='list_budgets'),
]
