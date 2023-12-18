from django.contrib import admin
from django.urls import path, include
from .views import RegistrationController, LogoutUserView
from budgets.views import BudgetListController

## МАППИНГ УРЛОВ И КОНТРОЛЛЕРОВ
urlpatterns = [
    path('', BudgetListController.as_view(), name="default_list_budgets"),
    path('register/', RegistrationController.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='custom_logout'),
    path('login/', include('django.contrib.auth.urls')),

]
