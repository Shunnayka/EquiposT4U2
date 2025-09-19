from django.contrib import admin
from django.urls import path
from equipos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('teams/', views.teams, name='teams'),
    path('teams/create/', views.create_team, name='create_team'),
    path('players/', views.players, name='players'),
    path('tasks/', views.tasks, name='tasks'),
]