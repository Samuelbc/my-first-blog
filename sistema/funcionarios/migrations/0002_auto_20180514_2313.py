# Generated by Django 2.0.2 on 2018-05-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='tipo',
            field=models.IntegerField(choices=[(1, 1), (2, 2)], default=1),
        ),
    ]
