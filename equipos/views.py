from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Team, Player, TrainingTask

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, '¡Registro exitoso!')
            return redirect('home')
        else:
            # Muestra errores del formulario
            for error in form.errors:
                messages.error(request, form.errors[error])
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def home(request):
    context = {}
    # Usa request.user.is_authenticated directamente en el template
    # en lugar de user_is_authenticated
    return render(request, 'home.html', context)

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente')
    return redirect('home')

@login_required
def teams(request):
    user_teams = Team.objects.filter(user=request.user)
    return render(request, 'teams.html', {'teams': user_teams})

@login_required
def create_team(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        league = request.POST.get('league')
        coach = request.POST.get('coach')
        team = Team.objects.create(
            name=name,
            league=league,
            coach=coach,
            user=request.user
        )
        messages.success(request, f'Equipo {name} creado exitosamente')
        return redirect('teams')
    return render(request, 'create_team.html')

@login_required
def players(request):
    user_players = Player.objects.filter(user=request.user)
    return render(request, 'players.html', {'players': user_players})

@login_required
def tasks(request):
    user_tasks = TrainingTask.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': user_tasks})