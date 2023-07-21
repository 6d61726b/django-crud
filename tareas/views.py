from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.
def inicio(request):
	return render(request, 'inicio.html')

def registrarse(request):
	if request.method == 'GET':
		return render(request, 'registrarse.html', {
			'form': UserCreationForm
		})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				usuario = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'])
				usuario.save()
				login(request, usuario)
				return redirect('tareas')
			except IntegrityError:
				return render(request, 'registrarse.html', {
					'form': UserCreationForm,
					'error': 'El usuario ya existe'
				})
		return render(request, 'registrarse.html', {
			'form': UserCreationForm,
			'error': 'La contraseña no coincide'
			})

def tareas(request):
	return render(request, 'tareas.html')