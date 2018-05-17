from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Create your models here.
class Funcionario(models.Model):
    TIPOS_FUNC = [(1,1),(2,2)]
    nome = models.CharField(max_length=200)
    tipo = models.IntegerField(choices=TIPOS_FUNC,default=1)
    med_comportamento = models.FloatField(default=0)
    med_rendimento = models.FloatField(default=0)
    erros_total = models.IntegerField(default=0, null=True)
    erro_etiqueta = models.IntegerField(default=0)
    porcentagem_etiqueta = models.FloatField(default=0)
    erro_falta = models.IntegerField(default=0)
    porcentagem_falta = models.FloatField(default=0)
    erro_troca = models.IntegerField(default=0)
    porcentagem_troca = models.FloatField(default=0)
    erro_sabor = models.IntegerField(default=0)
    porcentagem_sabor = models.FloatField(default=0)
    erro_vencido = models.IntegerField(default=0)
    porcentagem_vencido = models.FloatField(default=0)
    erro_brinde = models.IntegerField(default=0)
    porcentagem_brinde = models.FloatField(default=0)


    def __str__(self):
        return self.nome



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Comportamento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateField('date published')
    ordens = models.IntegerField(default=5)
    celular = models.IntegerField(default=5)
    pausa_indev = models.IntegerField(default=5)
    banco = models.IntegerField(default=5)
    media = models.FloatField(default=5, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dia = models.CharField(max_length=10, null=True)
    mes = models.CharField(max_length=10, null=True)
    ano = models.CharField(max_length=10, null=True)


def update_field_comportamento(sender, **kwargs):
    inst = kwargs['instance']
    func_profile = Funcionario.objects.filter(nome = inst.funcionario)
    comp_table = Comportamento.objects.filter(funcionario = inst.funcionario)
    med = 0
    cont = 0
    for entry in comp_table:
        med = med + entry.media
        cont= cont+1
    if cont == 0:
        func_profile.update(med_comportamento=0)
    else:
        func_profile.update(med_comportamento=med/cont)



post_save.connect(update_field_comportamento, sender=Comportamento)
post_delete.connect(update_field_comportamento, sender=Comportamento)



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Rendimento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateField('date published')
    total_diario = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dia = models.CharField(max_length=10, null=True)
    mes = models.CharField(max_length=10, null=True)
    ano = models.CharField(max_length=10, null=True)


def update_field_rendimento(sender, **kwargs):
    inst = kwargs['instance']
    func_profile = Funcionario.objects.filter(nome = inst.funcionario)
    rend_table = Rendimento.objects.filter(funcionario = inst.funcionario)
    parcial = 0
    cont = 0
    for entry in rend_table:
        parcial = parcial + entry.total_diario
        cont= cont + 1
    if cont != 0:
        func_profile.update(med_rendimento=parcial/cont)
    else:
        func_profile.update(med_rendimento=0)


post_save.connect(update_field_rendimento, sender=Rendimento)
post_delete.connect(update_field_rendimento, sender=Rendimento)


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Erros(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateField('date published')
    data_pedido = models.DateField('date published')
    pedido = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    erro = models.CharField(max_length=200)
    conta = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dia = models.CharField(max_length=10, null=True)
    mes = models.CharField(max_length=10, null=True)
    ano = models.CharField(max_length=10, null=True)
    dia_pedido = models.CharField(max_length=10, null=True)
    mes_pedido = models.CharField(max_length=10, null=True)
    ano_pedido = models.CharField(max_length=10, null=True)

def update_field_erro(sender, **kwargs):
    inst = kwargs['instance']
    func_profile = Funcionario.objects.filter(nome = inst.funcionario)
    total_erros = func_profile.erros_total
    t_e_etiqueta = func_profile.erro_etiqueta
    t_e_falta = func_profile.erro_falta
    t_e_troca = func_profile.erro_troca
    t_e_sabor = func_profile.erro_sabor
    t_e_vencido = func_profile.erro_vencido
    t_e_brinde = func_profile.erro_brinde


    if kwargs['created']:
        if inst.erro == 'etiqueta_trocada':
            func_profile.update(erro_etiqueta=t_e_etiqueta+1)
            func_profile.update(erros_total=total_erros+1)
            porcentagem_etiqueta = func_profile.erro_etiqueta/func_profile.erros_total

        elif inst.erro == 'falta_produto':
            func_profile.update(erro_falta=t_e_falta+1)
            func_profile.update(erros_total=total_erros+1)
            porcentagem_falta = func_profile.erro_falta/func_profile.erros_total

        elif inst.erro == 'produto_trocado':
            func_profile.update(erro_troca=t_e_troca+1)
            func_profile.update(erros_total=total_erros+1)
            porcentagem_troca = func_profile.erro_troca/func_profile.erros_total

        elif inst.erro == 'sabor_errado':
            func_profile.update(erro_sabor=t_e_sabor+1)
            func_profile.update(erros_total=total_erros+1)
            porcentagem_sabor = func_profile.erro_sabor/func_profile.erros_total

        elif inst.erro == 'produto_vencido':
            func_profile.update(erro_vencido=t_e_vencido+1)
            func_profile.update(erros_total=total_erros+1)
            porcentagem_vencido = func_profile.erro_vencido/func_profile.erros_total

        elif inst.erro == 'falta_brinde':
            func_profile.update(erro_brinde=t_e_brinde+1)
            func_profile.update(erros_total=total_erros+1)
            porcentagem_brinde = func_profile.erro_brinde/func_profile.erros_total

    else:
        if inst.erro == 'etiqueta_trocada':
            func_profile.update(erro_etiqueta=t_e_etiqueta-1)
            func_profile.update(erros_total=total_erros-1)
            porcentagem_etiqueta = func_profile.erro_etiqueta/func_profile.erros_total

        elif inst.erro == 'falta_produto':
            func_profile.update(erro_falta=t_e_falta-1)
            func_profile.update(erros_total=total_erros-1)
            porcentagem_falta = func_profile.erro_falta/func_profile.erros_total

        elif inst.erro == 'produto_trocado':
            func_profile.update(erro_troca=t_e_troca-1)
            func_profile.update(erros_total=total_erros-1)
            porcentagem_troca = func_profile.erro_troca/func_profile.erros_total

        elif inst.erro == 'sabor_errado':
            func_profile.update(erro_sabor=t_e_sabor-1)
            func_profile.update(erros_total=total_erros-1)
            porcentagem_sabor = func_profile.erro_sabor/func_profile.erros_total

        elif inst.erro == 'produto_vencido':
            func_profile.update(erro_vencido=t_e_vencido-1)
            func_profile.update(erros_total=total_erros-1)
            porcentagem_vencido = func_profile.erro_vencido/func_profile.erros_total

        elif inst.erro == 'falta_brinde':
            func_profile.update(erro_brinde=t_e_brinde-1)
            func_profile.update(erros_total=total_erros-1)
            porcentagem_brinde = func_profile.erro_brinde/func_profile.erros_total


post_save.connect(update_field_erro, sender=Erros)
post_delete.connect(update_field_erro, sender=Erros)
