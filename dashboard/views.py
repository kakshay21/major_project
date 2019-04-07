from django.shortcuts import render
from django.contrib.auth.models import User
from dashboard.models import Equipment, Usage, UserSettings

# Create your views here.

def dashboard(request):
    template_name = 'index.html'
    equipments = Equipment.objects.all().order_by('id').reverse()
    equipments_details = []
    for obj in equipments:
        equip_usage = Usage.objects.filter(equipment=obj)
        state = False
        if equip_usage.count() == 1:
            state = equip_usage[0].state
        equip_ = {
            'id': obj.id,
            'name': obj.name,
            'rating': obj.rating,
            'state': state,
            'priority': obj.priority
        }
        equipments_details.append(equip_)
    context = {'equipments': equipments_details}
    return render(request, template_name, context)


def budget(request):
    template_name = 'budget.html'
    user = User.objects.filter(username='akshay').first()
    user_settings = UserSettings.objects.filter(user=user).first()
    context = {'budgets': user_settings.budget}
    return render(request, template_name, context)


def index(request):
    index_name = 'login.html'
    return render(request, index_name, {})


def register(request):
    temp_name = 'register.html'
    return render(request, temp_name, {})


def add_equipment(request):
    temp_name = 'profile.html'
    return render(request, temp_name, {})
