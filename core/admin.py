from django.contrib import admin

from .models import Servico, Funcionario, Cargo, Recurso

@admin.register(Cargo)
class ModelCargo(admin.ModelAdmin):
    list_display = ['cargo', 'ativo', 'modificado']

@admin.register(Servico)
class ModelServicos(admin.ModelAdmin):
    list_display = ['servico', 'icone', 'ativo', 'modificado']

@admin.register(Funcionario)
class ModelFuncionario(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'ativo', 'modificado']

@admin.register(Recurso)
class ModelRecuso(admin.ModelAdmin):
    list_display = ['tecnologia', 'descricao', 'icone']
