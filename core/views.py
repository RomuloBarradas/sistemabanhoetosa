from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import PessoaForm


def index(request):
    return render(request, "index.html")
@login_required
def cadastro(request):
    pessoa_form = PessoaForm()
    return render(request, "cadastro.html", {"pessoa_form": pessoa_form})

"""def pessoa_novo(request):
     form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('index')
    else:
        messages.error(
            request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('index')
# Create your views here."""
