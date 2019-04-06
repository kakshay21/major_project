from django.shortcuts import render

# Create your views here.

def dashboard(request):
    template_name = 'index.html'
    return render(request, template_name, {})

def index(request):
    index_name = 'login.html'
    return render(request, index_name, {})

def register(request):
    temp_name = 'register.html'
    return render(request, temp_name, {})

def add_equipment(request):
    temp_name = 'add_equipment.html'
    return render(request, temp_name, {})