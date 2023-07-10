from django.contrib import admin
from django.urls import path, include
from done.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('done.urls')),
    path('',home, name='home'),
    
]
