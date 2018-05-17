from django.urls import path
from . import views



app_name = "anuncios"
urlpatterns = [
    path('', views.AnunciosView.as_view(), name='home'),
    path('addanuncio', views.AnunciosEntradaView.as_view(), name='entrada_anuncios')
]
