from django.shortcuts import render, redirect

# Create your views here.
def home(request,template='home.html'):
    return render(request, template)

def perfil(request,template='perfil.html'):
    return render(request, template)