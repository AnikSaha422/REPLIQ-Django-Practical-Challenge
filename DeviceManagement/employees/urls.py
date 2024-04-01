from django.urls import path
from .views.employeeView import EmployeeList, EmployeeDetail




urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
]
