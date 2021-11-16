from django.forms import ModelForm
from .models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'