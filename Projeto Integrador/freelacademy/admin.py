from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Configuração para o seu usuário aparecer de forma robusta no admin
class UsuarioAdmin(UserAdmin):
    # Campos que aparecerão na lista de usuários
    list_display = ('username', 'email', 'tipo', 'is_staff')
    
    # Adicionando seus campos customizados no formulário de edição
    fieldsets = UserAdmin.fieldsets + (
        ('Informações do FreelAcademy', {'fields': ('tipo', 'cpf_cnpj', 'telefone')}),
    )
    
    # Adicionando seus campos no formulário de criação
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações do FreelAcademy', {'fields': ('tipo', 'cpf_cnpj', 'telefone')}),
    )

# Registrando o modelo no painel
admin.site.register(Usuario, UsuarioAdmin)