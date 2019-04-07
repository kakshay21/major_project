"""iot_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dashboard.views import dashboard, index, register, add_equipment, budget
from dashboard.api import EquipmentResource
from django.contrib import admin
from django.urls import include, path
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(EquipmentResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', dashboard),
    path('index/', index),
    path('register/', register),
    path('add-equip/', add_equipment),
    path('budget/', budget),
    path('api/', include(v1_api.urls)),
]
