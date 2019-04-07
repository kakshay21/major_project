from django.shortcuts import render
from django.contrib.auth.models import User
from dashboard.models import Equipment, Usage, UserSettings


import datetime
# Create your views here.

def dashboard(request):
    template_name = 'index.html'
    equipments = Equipment.objects.all().order_by('id').reverse()
    equipments_details = []
    for obj in equipments:
        equip_usage = Usage.objects.filter(equipment=obj)
        state = False
        if equip_usage.count() > 0:
            equip_usage = equip_usage.first()
            state = equip_usage.state
            if state:
                stop_mins = datetime.datetime.now().time().hour*60 + datetime.datetime.now().time().minute
                start_mins = equip_usage.started_at.hour*60 + equip_usage.started_at.minute
                used_till_now =  stop_mins - start_mins
            else:
                used_till_now = equip_usage.used_mins
            equip_usage.percent = (used_till_now*100)/obj.max_mins
            equip_usage.save()
        equip_ = {
            'id': obj.id,
            'name': obj.name,
            'rating': obj.rating,
            'state': state,
            'priority': obj.priority,
            'usage_left': (used_till_now*100)/obj.max_mins,
            'amount': used_till_now*obj.rating*8/60000
        }
        equipments_details.append(equip_)
    sorted_equip = sorted(equipments_details, key=lambda k: k['usage_left'], reverse=True)
    context = {'equipments': equipments_details, 'notification':sorted_equip[0:4]}
    return render(request, template_name, context)


def budget(request):
    template_name = 'budget.html'
    user = User.objects.all().first()
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
