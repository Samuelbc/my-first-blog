from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView

from .models import Anuncio
from .forms import AnuForm




# Create your views here.
class AnunciosView(TemplateView):
    template_name = 'anuncios/basic_anuncios.html'

    def get(self, request):
        try:
            tab = Anuncio.objects.all()
        except:
            tab = 'Nenhuma entrada encontrada.'

        return render(request, 'anuncios/basic_anuncios.html', {'tab':tab})


class AnunciosEntradaView(TemplateView):
    template_name = 'anuncios/entrada_anuncios.html'

    def get(self, request):
        form = AnuForm()
        return render(request, 'anuncios/entrada_anuncios.html',{'form':form})

    def post(self, request):
        form = AnuForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            form = AnuForm()

        return render(request, 'anuncios/entrada_anuncios.html', {'form': form})
