from django.urls import path
from . import views
from .views import EmployeeView, EmployeeListView, EmployeeUpdateView, EmployeeDeleteView

# app_name = "employee"

urlpatterns = [
    path('', EmployeeListView, name='employee_list'),
    path('create/', EmployeeView, name='employee_create'),
    path('update/<int:pk>/', EmployeeUpdateView, name='employee_update'),
    path('delete/<int:pk>/', EmployeeDeleteView, name='employee_delete'),
    
    
    
    
]
