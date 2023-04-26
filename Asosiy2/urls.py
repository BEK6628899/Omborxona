from django.urls import path
from .views import *

urlpatterns = [
    path('statistika/', StatistikaView.as_view(), name='statistika'),
    path('statistika_ochir/<int:pk>/', StatistikaOchir.as_view(), name='stats_ochir'),
    # path('stats_update/<int:pk>/', StatistikaUpdate.as_view(), name='stats_update')
]

# path('mahsulot_update/<int:pk>/', MahsulotUpdate.as_view(), name='mahsulot_update'),