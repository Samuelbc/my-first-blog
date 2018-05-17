from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView

from .models import Expedicao
from .forms import ExpForm


# Create your views here.



class ExpedicaoView(TemplateView):
    template_name = 'expedicao/basic_exp.html'

    def get(self, request):
        try:
            tab = Expedicao.objects.all()
        except:
            tab = 'Nenhuma entrada encontrada.'

        return render(request, 'expedicao/basic_exp.html', {'tab':tab})


class ExpedicaoEntradaView(TemplateView):
    template_name = 'expedicao/entrada_expedicao.html'

    def get(self, request):
        form = ExpForm()
        return render(request, 'expedicao/entrada_expedicao.html',{'form':form})

    def post(self, request):
        form = ExpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            dia = form.cleaned_data['dia']
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            post.usuario = request.user
            post.data = ano+'-'+mes+'-'+dia
            post.save()
            form = ExpForm()

        return render(request, 'expedicao/entrada_expedicao.html', {'form': form})
