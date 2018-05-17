from django.urls import path
from . import views



app_name = "expedicao"
urlpatterns = [
    path('', views.ExpedicaoView.as_view(), name='home'),
    path('addexp', views.ExpedicaoEntradaView.as_view(), name='entrada_expedicao')
]
