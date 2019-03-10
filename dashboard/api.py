from django.conf.urls import url
from dashboard.models import Equipment
from tastypie.resources import ModelResource
from tastypie.utils.urls import trailing_slash
from tastypie.utils.timezone import now

import json


class EquipmentResource(ModelResource):
    class Meta:
        queryset = Equipment.objects.all()
        resource_name = 'equipment'
        allowed_methods = ['get', 'post']

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/equip%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_equipment'), name="api_get_equipment")
        ]

    def get_equipment(self, request, *args, **kwargs):
        counter = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
        return self.create_response(request, counter)
