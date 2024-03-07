from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from consignados.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo Email deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True')

        return self.create_user(email, password, **extra_fields)



class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome



class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True,max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    observacao = models.CharField(max_length=100,blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email


class Material(models.Model):
    nome = models.CharField(max_length=100,blank=False, null=False)
    lote = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Materiais"

    def __str__(self):
        return self.nome 

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nome

class Hospital(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Hospitais"

    def __str__(self):
        return self.nome
    

class Consignado(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE,blank=True, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,blank=True, null=True)
    vendedor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True, null=True)
    material = models.ManyToManyField(Material, blank=True)

    class Meta:
        verbose_name_plural = "Consignações"

    def __str__(self):
        return self.paciente
    

    

class SaidaAvulsa(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE,blank=True, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,blank=True, null=True)
    vendedor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True, null=True)
    

    class Meta:
        verbose_name_plural = "Saidas Avulsa"

    def __str__(self):
        return self.paciente

class ItensSaida(models.Model):
    vendedor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True, null=True)
    material = models.ForeignKey(Material, blank=False,null=False,on_delete=models.CASCADE)
    quantiade = models.IntegerField(blank=True, null=True)
    saidaAvulsa = models.ForeignKey(SaidaAvulsa, on_delete=models.CASCADE,blank=True, null=True)
    class Meta:
        verbose_name_plural = "Itens Saidas Avulsa"
    def __str__(self):
        return str(self.material)