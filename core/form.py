from django.db import models
from django.forms import ModelForm, fields
from .models import Pessoa,Animal,BanhoeTosa


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class BanhoeTosaForm(ModelForm):
    class Meta:
        model = BanhoeTosa
        fields = '__all__'