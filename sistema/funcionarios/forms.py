from django import forms
from .models import Funcionario, Comportamento, Rendimento, Erros



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

ORDEM_CHOICES = [('Nome','Nome'),('Comportamento','Comportamento'),('Rendimento','Rendimento'),('Erros','Erros')]


class OrderForm(forms.Form):
    ordem = forms.ChoiceField(choices=ORDEM_CHOICES)
    ordem.widget.attrs.update({'class': 'form-control'})

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


DIA_CHOICES = [('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08')
,('09','09'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),
('20','20'),('30','30'),('31','31')]
MES_CHOICES = [('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),
('09','09'),('10','10'),('11','11'),('12','12')]
ANO_CHOICES = [('2018','2018'),('2019','2019')]
COMP_CHOICES = [(5,5),(0,0),(1,1),(2,2),(3,3),(4,4),(6,6),(7,7),(8,8),(9,9),(10,10)]


class CompForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(Funcionario.objects.all())
    banco = forms.ChoiceField(choices=COMP_CHOICES)
    ordens = forms.ChoiceField(choices=COMP_CHOICES)
    ajuda = forms.ChoiceField(choices=COMP_CHOICES)
    celular = forms.ChoiceField(choices=COMP_CHOICES)
    pausa_indev = forms.ChoiceField(choices=COMP_CHOICES)
    dia = forms.ChoiceField(choices=DIA_CHOICES)
    mes = forms.ChoiceField(choices=MES_CHOICES)
    ano = forms.ChoiceField(choices=ANO_CHOICES)


    dia.widget.attrs.update({'class': 'form-control col-md'})
    mes.widget.attrs.update({'class': 'form-control col-md'})
    ano.widget.attrs.update({'class': 'form-control col-md'})
    funcionario.widget.attrs.update({'class': 'form-control col-md-5'})
    banco.widget.attrs.update({'class': 'form-control col-md-5'})
    ordens.widget.attrs.update({'class': 'form-control col-md-5'})
    ajuda.widget.attrs.update({'class': 'form-control col-md-5'})
    celular.widget.attrs.update({'class': 'form-control col-md-5'})
    pausa_indev.widget.attrs.update({'class': 'form-control col-md-5'})

    class Meta:
        model = Comportamento
        fields =  ('funcionario','ordens','ajuda','celular','pausa_indev','dia','mes','ano')




#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class RendForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(Funcionario.objects.filter(tipo=2))
    total_diario = forms.IntegerField()
    dia = forms.ChoiceField(choices=DIA_CHOICES)
    mes = forms.ChoiceField(choices=MES_CHOICES)
    ano = forms.ChoiceField(choices=ANO_CHOICES)


    total_diario.widget.attrs.update({'class': 'form-control col-md-5'})
    dia.widget.attrs.update({'class': 'form-control col-md'})
    mes.widget.attrs.update({'class': 'form-control col-md'})
    ano.widget.attrs.update({'class': 'form-control col-md'})
    funcionario.widget.attrs.update({'class': 'form-control col-md-5'})


    class Meta:
        model = Rendimento
        fields =  ('funcionario','total_diario','dia','mes','ano')




#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

CONTA_CHOICES = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(1,1),(12,12)]
ERRO_CHOICES = [('etiqueta_trocada','Etiqueta trocada'),('falta_produto','Faltando produto'),
    ('produto_trocado','Produto trocado'),('sabor_errado','Sabor Errado'),
    ('produto_vencido','Produto vencido'),('falta_brinde','Faltando brinde')]

class ErroForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(Funcionario.objects.filter(tipo=2))
    dia = forms.ChoiceField(choices=DIA_CHOICES)
    mes = forms.ChoiceField(choices=MES_CHOICES)
    ano = forms.ChoiceField(choices=ANO_CHOICES)
    dia_pedido = forms.ChoiceField(choices=DIA_CHOICES)
    mes_pedido = forms.ChoiceField(choices=MES_CHOICES)
    ano_pedido = forms.ChoiceField(choices=ANO_CHOICES)
    pedido = forms.CharField(max_length=200)
    cliente = forms.CharField(max_length=200)
    erro = forms.ChoiceField(choices=ERRO_CHOICES)
    conta = forms.ChoiceField(choices=CONTA_CHOICES)

    funcionario.widget.attrs.update({'class': 'form-control col-md-5'})
    dia.widget.attrs.update({'class': 'form-control col-md'})
    mes.widget.attrs.update({'class': 'form-control col-md'})
    ano.widget.attrs.update({'class': 'form-control col-md'})
    dia_pedido.widget.attrs.update({'class': 'form-control col-md'})
    mes_pedido.widget.attrs.update({'class': 'form-control col-md'})
    ano_pedido.widget.attrs.update({'class': 'form-control col-md'})
    pedido.widget.attrs.update({'class': 'form-control col-md-5'})
    cliente.widget.attrs.update({'class': 'form-control col-md-5'})
    erro.widget.attrs.update({'class': 'form-control col-md-5'})
    conta.widget.attrs.update({'class': 'form-control col-md-5'})

    class Meta:
        model = Erros
        fields =  ('funcionario','pedido','cliente','erro','conta','dia','mes','ano','dia_pedido','mes_pedido','ano_pedido')
