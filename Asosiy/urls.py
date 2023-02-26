from django.urls import path
from .views import *

urlpatterns = [
    path('bolim/', BolimlarView.as_view(),name='bolim'),   #Asosiy/bolim
    path('mahsulotlar/', MahsulotlarView.as_view(),name='mahsulotlar'),   #Asosiy/bolim/mahsulotlar
    path('mahsulot_ochir/<int:pk>/', MahsulotOchir.as_view(),name='mahsulot_ochir'),
    path('mahsulot_update/<int:pk>/', MahsulotUpdate.as_view(),name='mahsulot_update'),
    path('client/', ClientView.as_view(),name='client'),
    path('client_ochir/<int:pk>/', ClientOchir.as_view(), name='client_ochir'),
    path('client_update/<int:pk>/', ClientUpdate.as_view(), name='client_update'),
]








