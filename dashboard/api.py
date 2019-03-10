from django.conf.urls import url
from dashboard.models import Equipment, User
from tastypie.resources import ModelResource
from tastypie.utils.urls import trailing_slash
from tastypie.utils.timezone import now

import json


class EquipmentResource(ModelResource):
    class Meta:
        queryset = Equipment.objects.all()
        equipment_resource = 'equipment'
        user_resource = 'user'
        allowed_methods = ['get', 'post']

    def prepend_urls(self):
        return [
            url(r"^(?P<equipment_resource>%s)/equip%s$" %
                (self._meta.equipment_resource, trailing_slash()),
                self.wrap_view('get_equipment'), name='api_get_equipment'),
            url(r"^(?P<user_resource>%s)/login%s$" %
                (self._meta.user_resource, trailing_slash()),
                self.wrap_view('validate_user'), name='api_validate_user')
        ]

    def get_equipment(self, request, *args, **kwargs):
        result = {'name': 'tubelight', 'rating': 150}
        return self.create_response(request, result)
    
    def validate_user(self, request, *args, **kwargs):
        body = json.loads(request.body)
        result = {'status': True, 'body': body}
        return self.create_response(request, result)
