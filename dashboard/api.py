from django.conf.urls import url
from django.utils import timezone
from dashboard.models import Equipment, User, Usage
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
            url(r"^(?P<equipment_resource>%s)/switch%s$" %
                (self._meta.equipment_resource, trailing_slash()),
                self.wrap_view('toggle_equipment'), name='api_toggle_equipment'),
            url(r"^(?P<equipment_resource>%s)/add%s$" %
                (self._meta.equipment_resource, trailing_slash()),
                self.wrap_view('add_equipment'), name='api_add_equipment'),
            url(r"^(?P<user_resource>%s)/login%s$" %
                (self._meta.user_resource, trailing_slash()),
                self.wrap_view('validate_user'), name='api_validate_user')
        ]

    def validate_key(self, body, key):
        if not body or key not in body:
            result = {'status':False, 'message': 'Expected equipment {0}'.format(key)}
            return result
        equipment = Equipment.objects.filter(id=body[key])
        if equipment.count() < 1:
            result = {'status':False, 'message': 'Equipment {0} does not exist'.format(key)}
            return result
        return {'status': True, 'query': equipment[0]}

    def get_equipment(self, request, *args, **kwargs):
        body = json.loads(request.body)
        result = self.validate_key(body, 'id')
        if not result['status']:
            return self.create_response(request, result)
        equipment = result['query']
        response = {
            'name': equipment.name,
            'rating': equipment.rating,
            'priority': equipment.priority
        }
        return self.create_response(request, response)

    def toggle_equipment(self, request, *args, **kwargs):
        # equip_id, status
        body = json.loads(request.body)
        result = self.validate_key(body, 'id')
        if not result['status']:
            return self.create_response(request, result)
        equipment = result['query']
        equipment_usage = Usage.objects.filter(equipment=equipment)
        if equipment_usage.count() < 1:
            result = {'status':False, 'message': '{0}\'s usage does not exist'.format(equipment.name)}
            return self.create_response(request, result)
        equipment_usage = equipment_usage[0]
        required_state = body.get('state')
        if not equipment_usage.state and required_state:
            equipment_usage.state = required_state
            equipment_usage.started_at = timezone.now()
            equipment_usage.save()
            # TODO: toggle gpio switch
        if equipment_usage.state and not required_state:
            equipment_usage.state = required_state
            equipment_usage.stopped_at = timezone.now()
            equipment_usage.save()
            # TODO: toggle gpio switch
        result = {
            'name': equipment.name,
            'state': equipment_usage.state,
            'usage': equipment_usage.stopped_at - equipment_usage.started_at
        }
        return self.create_response(request, result)

    def add_equipment(self, request, *args, **kwargs):
        body = json.loads(request.body)
        name = body.get('name')
        if not name:
            result = {'status':False, 'message': 'Equipment name must not be empty'}
            return self.create_response(request, result)
        rating = body.get('rating')
        if not rating:
            result = {'status':False, 'message': 'Equipment rating must not be empty'}
            return self.create_response(request, result)
        priority = body.get('priority')
        if not priority:
            priority = 0
        equipment = Equipment(name=name, rating=rating, priority=priority)
        equipment.save()
        response = {'status': True, 'message': '{0} is successfully added'.format(name)}
        return self.create_response(request, response)

    def validate_user(self, request, *args, **kwargs):
        body = json.loads(request.body)
        # think about good authentication module
        result = {'status': True, 'body': body}
        return self.create_response(request, result)
