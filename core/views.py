from django.shortcuts import render
from core.models import Evento


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    # evento = Evento.objects.get(id=1) traz apenas um único dado
    # usuario = request.user pega dados do usuário logado
    # evento = Evento.objects.filter(usuario=usuario)  realiza a busca dos dados pelo usuário logado
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
