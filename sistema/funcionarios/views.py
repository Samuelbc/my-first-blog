from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import TemplateView
from datetime import datetime

from .models import Funcionario, Comportamento, Erros, Rendimento
from .forms import OrderForm, CompForm, RendForm, ErroForm

# Create your views here.

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class HomeView(TemplateView):
    template_name = 'funcionarios/home.html'

    def get(self, request):
        funcs =  Funcionario.objects.order_by('nome')
        form = OrderForm()
        return render(request, 'funcionarios/home.html', {'funcs': funcs, 'form': form})

    def post(self, request):
        funcs =  Funcionario.objects.order_by('nome')
        form = OrderForm(request.POST)
        if form.is_valid():
            ordem = form.cleaned_data['ordem']
            if ordem == 'Rendimento':
                funcs =  Funcionario.objects.order_by('med_rendimento')
            elif ordem == 'Comportamento':
                funcs =  Funcionario.objects.order_by('med_comportamento')
            elif ordem == 'Erros':
                funcs =  Funcionario.objects.order_by('med_erros')
            else:
                funcs =  Funcionario.objects.order_by('nome')

        return render(request, 'funcionarios/home.html', {'funcs': funcs, 'form': form})

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class BasicFuncView(TemplateView):
    template_name = 'funcionarios/basic_func.html'

    def get(self, request, func_nome):
        func = get_object_or_404(Funcionario, nome=func_nome)
        funcs =  Funcionario.objects.order_by('nome').exclude(nome=func_nome)
        return render(request, 'funcionarios/basic_func.html', {'func': func,'funcs': funcs})

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class FuncComportamento(TemplateView):
    template_name = 'funcionarios/comportamento.html'

    def get(self, request, func_nome):
        func = get_object_or_404(Funcionario, nome=func_nome)
        funcs =  Funcionario.objects.order_by('nome').exclude(nome=func_nome)
        try:
            tab = Comportamento.objects.filter(funcionario=func.id)
        except:
            tab = 'Nenhuma entrada encontrada.'

        return render(request, 'funcionarios/comportamento.html', {'func': func, 'funcs':funcs, 'tab':tab})


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class FuncErro(TemplateView):
    template_name = 'funcionarios/erros.html'

    def get(self, request, func_nome):
        func = get_object_or_404(Funcionario, nome=func_nome)
        funcs =  Funcionario.objects.order_by('nome').exclude(nome=func_nome)
        try:
            tab = Rendimento.objects.filter(funcionario=func.id)
        except:
            tab = 'Nenhuma entrada encontrada.'

        return render(request, 'funcionarios/erros.html', {'func': func, 'funcs':funcs, 'tab':tab})

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class FuncRendimento(TemplateView):
    template_name = 'funcionarios/rendimento.html'

    def get(self, request, func_nome):
        func = get_object_or_404(Funcionario, nome=func_nome)
        funcs =  Funcionario.objects.order_by('nome').exclude(nome=func_nome)
        try:
            tab = Erros.objects.filter(funcionario=func.id)
        except:
            tab = 'Nenhuma entrada encontrada.'

        return render(request, 'funcionarios/rendimento.html', {'func': func, 'funcs':funcs, 'tab':tab})

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class EntComp(TemplateView):
    template_name = 'funcionarios/entrada_comportamento.html'

    def get(self, request):
        form = CompForm()
        return render(request, 'funcionarios/entrada_comportamento.html', {'form': form})

    def post(self, request):
        form = CompForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            dia = form.cleaned_data['dia']
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            post.media = ((post.ordens*2)+(post.banco*3)+(post.celular)+(post.pausa_indev))/7
            post.usuario = request.user
            post.data = ano+'-'+mes+'-'+dia
            post.save()
            form = CompForm()

        return render(request, 'funcionarios/entrada_comportamento.html', {'form': form})


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class EntRend(TemplateView):
    template_name = 'funcionarios/entrada_rendimento.html'

    def get(self, request):
        form = RendForm()
        return render(request, 'funcionarios/entrada_rendimento.html', {'form': form})

    def post(self, request):
        form = RendForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            dia = form.cleaned_data['dia']
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            post.usuario = request.user
            post.data = ano+'-'+mes+'-'+dia
            post.save()
            form = RendForm()

        return render(request, 'funcionarios/entrada_rendimento.html', {'form': form})


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class EntErro(TemplateView):
    template_name = 'funcionarios/entrada_erro.html'

    def get(self, request):
        form = ErroForm()
        return render(request, 'funcionarios/entrada_erro.html', {'form': form})

    def post(self, request):
        form = ErroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            dia = form.cleaned_data['dia']
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            dia_pedido = form.cleaned_data['dia_pedido']
            mes_pedido = form.cleaned_data['mes_pedido']
            ano_pedido = form.cleaned_data['ano_pedido']
            post.usuario = request.user
            post.data_pedido = ano_pedido+'-'+mes_pedido+'-'+dia_pedido
            post.data = ano+'-'+mes+'-'+dia
            post.save()
            form = ErroForm()

        return render(request, 'funcionarios/entrada_erro.html', {'form': form})

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
