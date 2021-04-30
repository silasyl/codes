# Aula 01: Introdução e ambiente Django
Cmder:
cd C:\Users\Silas\PycharmProjects\virtualenvs
python -m venv dev_django
# Criar uma virtual env (ambiente com versões controladas)

cd .\dev_django\
.\Scripts\activate
# Ativa a virtual env no terminal

pip install django
# Instala o django na virtual env

cd C:\Users\Silas\PycharmProjects
# Diretório para os projetos

django-admin startproject hello_django
# Cria o projeto

Pycharm:
File > Settings:
Busca: interpreter > Python Interpreter
Python Interpreter: Show All...
+ > Existing environment > C:\Users\Silas\PycharmProjects\virtualenvs\dev_django\Scripts\python.exe
OK
OK
Apply > OK

manage.py:
Botão direito: Run 'manage'
Em cima: Edit configurations:
Parameters: runserver
OK

Comando igual no terminal:
cd .\hello_django\
python manage.py runserver

Terminal:
django-admin startapp core
# Cria app / dir core

hello_django > settings.py:
INSTALLED_APPS = [
	'core',

hello_django > urls.py:
from core import views
urlpatterns = [
	path('hello/<nome>/<int:idade>', views.hello),

core > migrations > views.py:
from django.shortcuts import render, HttpResponse
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))


## Aula 02: Estrutura básica e Django-admin
# django-admin.py
É o utilitário de linha de comando do Django para tarefas administrativas

# manage.py
É um wrapper em volta do django-admin.py
Ele delega tarefas para o django-admin.py
Responsável por colocar o pacote do projeto no sys.path
Ele define a variável de ambiente DJANGO_SETTINGS_MODULE que então aponta para o arquivo settings.py
Por isso, o manage.py é gerado automaticamente junto ao projeto, para facilitar o uso de comandos do django-admin.py

# wsgi.py
Web Server Gateway Interface - Interface de porta de entrada do servidor Web
Plataforma padrão para aplicações web em Python
Serve de interface do Servidor Web e a Aplicação Web
O Django com o comando startproject inicia uma configuração WSGI padrão para que se possa executar sua aplicação web
Quando se inicia a aplicação Django com o comando runserver é iniciado um servidor de aplicação web leve. Esse servidor é especificado pela configuração WSGI_APPLICATION

# settings.py
É o responsável pelas configurações do Django
Nele é possível configurar por exemplo apps, conexão com banco de dados, templates, time zone, cache, segurança, arquivos estáticos, etc.

# urls.py
É um Schema de URL
Responsável por gerenciar as Rotas da URLs, onde é possível configurar pra onde cada rota será executada
É uma forma limpa e elegante para gerenciar URLs

# views.py
Responsável por processar e retornar uma resposta para o cliente que fez a requisição

# models.py
Define o modelo de dados inteiramente em Python
Faz a abstração dos objetos de banco para o Python, transformando todas as tabelas em classes e os acessos são feitos utilizando linguagem Python, onde o Django realiza a transformação para SQL

# admin.py
Interface administrativa gerada automaticamente pelo Django
Ele lê os metadados que estão nos models e fornece uma interface poderosa e pronta para manipulação de dados

# static
Responsável por armazenar os arquivos estáticos
CSS, JavaScript, imagens

# templates
Responsável por armazenar os arquivos HTML
O diretório templates é diretório padrão para armazenarmos todo o conteúdo HTML da nossa aplicação


## Criar tabela
Terminal:
python manage.py migrate

## Criar superusuário
python manage.py createsuperuser --username admin


models.py:
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # define nome da tabela a ser criada quando migrada
    class Meta:
        db_table = 'evento'

    # faz aparecer titulo no bd
    def __str__(self):
        return self.titulo

Terminal:
python manage.py makemigrations core
# Criou o arquivo 0001_initial.py em core > migration

python manage.py sqlmigrate core 0001
# Migração do BD específico, no caso 0001

python manage.py migrate core 0001
# Implementa no BD

core > admin.py:
from core.models import Evento
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario',)

admin.site.register(Evento, EventoAdmin)


## Aula 03: Criando uma página de listagem
agenda > New Directory > templates
templates > New > HTML File > agenda.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Agenda</title>
</head>
<body>
    <h2>Agendamentos</h2>

    <b>{{evento.titulo}} - {{evento.data_evento}}</b>

    <ul style="font-size: 18px">
    {% for evento in eventos %}
        <li>{{evento.titulo}} - {{evento.get_data_evento}}</li>
    {% endfor %}
    </ul>

</body>
</html>


core > views.py:
from core.models import Evento

def lista_eventos(request):
    evento = Evento.objects.get(id=1)
    response = {'evento': evento}
    return render(request, 'agenda.html', response)

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


agenda > urls.py:
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos)


agenda > settings.py:
TEMPLATE = [
'DIRS': [os.path.join(BASE_DIR, 'templates')],


core > models.py:
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')


# template para páginas web via Django
templates:
agenda.html:
{% extends "model-page.html" %}

{% block content %}
    <h2>Agendamentos</h2>

    <ul style="font-size: 18px">
    {% for evento in eventos %}
        <li>{{evento.titulo}} - {{evento.get_data_evento}}</li>
    {% endfor %}
    </ul>
{% endblock %}


model.page.html:
<!DOCTYPE html>
<html lang="en">
<head>
    {% include "model-header.html" %}
</head>
<body>
    {% block content %} {% endblock %}
    {% include "model-footer.html" %}
</body>
</html>


model.header.html:
    <meta charset="UTF-8">
    <title>Agenda</title>
    <h1>Agenda</h1>


model.footer.html:
<p>Desenvolvido por Rafael Galleani</p>


# Arrumando problema de index retornando erro
agenda > urls.py:
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', views.index)
]

core > views.py:
def index(request):
    return redirect('/agenda/')


# Ou apenas na urls.py:
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/'))
]


## Aula 04: Autenticação e inserção de dados
# Autenticação, login e decoradores

header.html:
    <meta charset="UTF-8">
    <title>Agenda</title>
    <div align="right">
        <a href="/logout">logout</a>
    </div>
    <h1>Agenda</h1>


login.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Agenda</title>
</head>
<body>
    <h1>Login</h1>
    <form action="submit" method="POST">{% csrf_token %}
        <div align="center">
            <label>Usuário:</label>
            <input type="text" name="username">
            <label>Password:</label>
            <input type="password" name="password">
            <button type="submit">Entrar</button>
        </div>
    </form>
</body>
</html>


urls.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]


views.py:
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    else:
        redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


# Inserção de dados
agenda.html:
{% extends "model-page.html" %}

{% block content %}
    <h2>Agendamentos</h2>
    <a href="evento/">
        <button type="button">Novo Evento</button>
    </a>
    <ul style="font-size: 18px">
    {% for evento in eventos %}
        <li>{{evento.titulo}} - {{evento.get_data_evento}}</li>
    {% endfor %}
    </ul>
{% endblock %}


evento.html:
{% extends "model-page.html" %}

{% block content %}

<h2>Evento</h2>

<form action="submit" method="POST">{% csrf_token %}
    <label>Título</label>
    <br>
    <input type="text" name="titulo" size="22">
    <br>
    <label>Data do Evento:</label>
    <br>
    <input type="datetime-local" name="data_evento">
    <br>
    <label>Descrição</label>
    <br>
    <textarea name="descricao" rows="5" cols="24"></textarea>
    <br><br>
    <button type="submit">Salvar</button>
    <a href="/">
        <button type="button">Cancelar</button>
    </a>
</form>

{% endblock %}


urls.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/evento', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]


views.py:
@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')


## Aula 05: Alteração, exclusão e filtro de dados
# Alteração e exclusão de dados
agenda.html:
{% extends "model-page.html" %}

{% block content %}
    <h2>Agendamentos</h2>
    <a href="evento/">
        <button type="button">Novo Evento</button>
    </a>
    <ul style="font-size: 18px">
    {% for evento in eventos %}
        <li>
            {{evento.titulo}} - {{evento.get_data_evento}}
            ( <a href="evento/?id={{ evento.id }}">Editar</a>
            / <a href="evento/delete/{{ evento.id }}/">Excluir</a> )
        </li>
    {% endfor %}
    </ul>
{% endblock %}


evento.html:
{% extends "model-page.html" %}

{% block content %}

<h2>Evento</h2>

<form action="submit" method="POST">{% csrf_token %}
    <label>Título</label>
    <input type="number" name="id_evento" value="{{ evento.id }}" hidden>
    <br>
    <input type="text" name="titulo" size="22" value="{{ evento.titulo }}">
    <br>
    <label>Data do Evento:</label>
    <br>
    <input type="datetime-local" name="data_evento" value="{{evento.get_data_input_evento}}">
    <br>
    <label>Descrição</label>
    <br>
    <textarea name="descricao" rows="5" cols="24">{{evento.descricao}}</textarea>
    <br><br>
    <button type="submit">Salvar</button>
    <a href="/">
        <button type="button">Cancelar</button>
    </a>
</form>

{% endblock %}


urls.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]


views.py:
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')


core > admin.py:
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario',)


models.py:
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')


# Filtros, tipos de responses, JSON
agenda.html:
{% extends "model-page.html" %}

{% block content %}
    <h2>Agendamentos</h2>
    <a href="evento/">
        <button type="button">Novo Evento</button>
    </a>
    <ul style="font-size: 18px">
    {% for evento in eventos %}
        <li>
            <div style={% if evento.get_evento_atrasado %}
                            "color:red"
                        {% endif %}>
                {{evento.titulo}} - {{evento.get_data_evento}}
                ( <a href="evento/?id={{ evento.id }}">Editar</a>
                / <a href="evento/delete/{{ evento.id }}/">Excluir</a> )
            </div>
        </li>
    {% endfor %}
    </ul>
{% endblock %}


views.py:
from datetime import datetime, timedelta

@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=user,
                                   data_evento__gt=data_atual)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


models.py:
from datetime import datetime

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False


settings.py:
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_TZ = False

# Msg de erro para urls errados
views.py:
from django.http.response import Http404

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


# JSON
views.py:
from django.contrib.auth.models import User
from django.http.response import Http404, JsonResponse

def json_lista_evento(request, id_usuario):
    user = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=user).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)


urls.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/<int:id_usuario>/', views.json_lista_evento),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)
]
