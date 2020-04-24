from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(resquest):
    if resquest.POST:
        username = resquest.POST.get('username')
        password = resquest.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(resquest, usuario)
            return redirect('/')
        else:
            messages.error(resquest, "Usuário ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    # evento = Evento.objects.get(id=1) traz apenas um único dado
    # pega dados do usuário logado
    usuario = request.user
    # realiza a busca dos dados pelo usuário logado
    evento = Evento.objects.filter(usuario=usuario)
    # evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
