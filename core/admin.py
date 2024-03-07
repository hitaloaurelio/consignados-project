from django.contrib import admin
from .models import Empresa, Material, Medico,Hospital,Consignado,SaidaAvulsa,ItensSaida
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lote','empresa')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'empresa')

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')


class ConsignadoAdmin(admin.ModelAdmin):
    list_display = ( 'hospital','data','vendedor')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('vendedor__first_name')

admin.site.register(Consignado, ConsignadoAdmin)


class SaidaAvulsaAdmin(admin.ModelAdmin):
    list_display = ( 'hospital','data','vendedor')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('vendedor__first_name')

admin.site.register(SaidaAvulsa, SaidaAvulsaAdmin)



class ItensSaidaAdmin(admin.ModelAdmin):
    list_display = ('material','quantiade', 'vendedor')

admin.site.register(ItensSaida, ItensSaidaAdmin)





# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     # search_fields = ['email']
#     form = EmailAuthenticationForm

#     # Campos a serem exibidos na lista de usuários no painel administrativo
#     list_display = ('email', )
#     # Campos a serem usados para pesquisar usuários no painel administrativo
#     search_fields = ('email', 'observacao')
#     # Campos a serem usados para filtrar usuários no painel administrativo
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
#     # Campos para exibir detalhes do usuário ao visualizar no painel administrativo
#     fieldsets = (
#         (None, {'fields': ('username', 'password',)}),
#         ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'observacao')}),
#         ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
#     )
#     # Campos a serem exibidos no formulário de criação de usuários no painel administrativo
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username' ,'password1', 'password2', 'is_staff', 'is_superuser'),
#         }),
#     )
#     # Campos a serem usados para ordenar usuários no painel administrativo
#     ordering = ('email',)

# # Registrar o modelo CustomUser no admin
# admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email', )
    ordering = ('email',)

    list_display = ( 'first_name','email', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'password','empresa','observacao')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Removendo a exibição do modelo de grupo na administração, uma vez que não precisamos dele
# admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
# from .forms import EmailAuthenticationForm

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     search_fields = ['email']
#     form = EmailAuthenticationForm

# admin.site.register(CustomUser, CustomUserAdmin)


