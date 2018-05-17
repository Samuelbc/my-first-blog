from django import forms
from .models import Expedicao

DIA_CHOICES = [('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08')
,('09','09'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),
('20','20'),('30','30'),('31','31')]
MES_CHOICES = [('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),
('09','09'),('10','10'),('11','11'),('12','12')]
ANO_CHOICES = [('2018','2018'),('2019','2019')]


class ExpForm(forms.ModelForm):
    dia = forms.ChoiceField(choices=DIA_CHOICES)
    mes = forms.ChoiceField(choices=MES_CHOICES)
    ano = forms.ChoiceField(choices=ANO_CHOICES)
    primeiro_tempo = forms.IntegerField()
    segundo_tempo = forms.IntegerField()
    terceiro_tempo = forms.IntegerField()
    quarto_tempo = forms.IntegerField()
    total = forms.IntegerField()

    dia.widget.attrs.update({'class': 'form-control col-md'})
    mes.widget.attrs.update({'class': 'form-control col-md'})
    ano.widget.attrs.update({'class': 'form-control col-md'})
    primeiro_tempo.widget.attrs.update({'class': 'form-control col-md-5'})
    segundo_tempo.widget.attrs.update({'class': 'form-control col-md-5'})
    terceiro_tempo.widget.attrs.update({'class': 'form-control col-md-5'})
    quarto_tempo.widget.attrs.update({'class': 'form-control col-md-5'})
    total.widget.attrs.update({'class': 'form-control col-md-5'})

    class Meta:
        model = Expedicao
        fields = {'primeiro_tempo','segundo_tempo','terceiro_tempo','quarto_tempo','total'}
