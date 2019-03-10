from django.shortcuts import render

# Create your views here.

def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name, {})
