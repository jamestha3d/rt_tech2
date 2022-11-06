from django.urls import path
from . import views

urlpatterns = [
    path('', views.listEmployees),
    path('add/', views.addEmployee, name="add"),
    path('delete/<str:pk>/', views.deleteEmployee, name="delete"),
    path('search/<str:last_name>/<int:dept_id>',views.searchEmployee, name="search"),
    path('departments/', views.listDepartments, name="departments"),
]