from django.urls import path
from report.views import *

app_name = 'report'

urlpatterns = [
    path('', show_reports, name='show_reports'),
    path('json/', show_json, name='show_json'),
    path('add-report/', add_report, name='add_report'),
    path('delete-report/<int:id>/', delete_report, name='delete_report'),
]