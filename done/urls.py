from django.urls import path
from . import views

app_name = 'done'

urlpatterns = [
    path('add-emp/', views.emp_add, name='add-emp'),
    path('roles/', views.role_management, name='role_management'),
    path('roles/<str:role>/toggle/', views.toggle_role, name='toggle_role'),
    path('delete-emp/<str:code>/', views.delete_emp, name='delete-emp'),
    path('update-emp/<str:code>/', views.update_emp, name='update-emp'),
]
