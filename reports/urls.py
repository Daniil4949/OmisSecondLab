from django.contrib import admin
from django.urls import path, include
from .views import ReportController, ReportListController, delete_report

## МАППИНГ УРЛОВ И КОНТРОЛЛЕРОВ
urlpatterns = [
    path('create_report/', ReportController.as_view(), name='create_report'),
    path('delete_report/<int:pk>/', delete_report, name='delete_report'),
    path('list_reports/', ReportListController.as_view(), name='list_reports'),
]
