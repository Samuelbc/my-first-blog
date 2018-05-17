from django import forms
from .models import Anuncio


class AnuForm(forms.ModelForm):
    produto = forms.CharField()
    marca = forms.CharField()
    reposicao = forms.BooleanField()


    produto.widget.attrs.update({'class': 'form-control col-md-3'})
    marca.widget.attrs.update({'class': 'form-control col-md-3'})
    reposicao.widget.attrs.update({'class': 'form-control col-sm-1'})

    class Meta:
        model = Anuncio
        fields = {'produto','marca','reposicao'}
