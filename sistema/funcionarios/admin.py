from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Funcionario)
admin.site.register(models.Comportamento)
admin.site.register(models.Erros)
admin.site.register(models.Rendimento)
admin.site.site_header = 'Administration'
