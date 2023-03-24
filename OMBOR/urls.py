from django.contrib import admin
from django.urls import path, include
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register),
    path('login/', Loginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('Asosiy/',include('Asosiy.urls')),
    path('Asosiy2/',include('Asosiy2.urls')),
]

