# Generated by Django 2.0.2 on 2018-05-16 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0007_auto_20180515_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='comportamento',
            name='ano',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='comportamento',
            name='dia',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='comportamento',
            name='mes',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='erros',
            name='ano',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='erros',
            name='ano_pedido',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='erros',
            name='dia',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='erros',
            name='dia_pedido',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='erros',
            name='mes',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='erros',
            name='mes_pedido',
            field=models.CharField(max_length=10, null=True),
        ),
    ]