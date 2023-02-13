from django.shortcuts import render
from .logic import measurements_logic as meu
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def meaurements_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            measurement = meu.get_measurement(id)
            measurement_dto = serializers.serialize('json', [measurement])
            return HttpResponse(measurement_dto, 'application/json')
        else:
            measurements = meu.get_measurements()
            measurements_dto = serializers.serialize('json', measurements)
            return HttpResponse(measurements_dto, 'application/json')

    if request.method == 'POST':
        measurement = meu.create_measurement(json.loads(request.body))
        measurement_dto = serializers.serialize('json', [measurement])
        return HttpResponse(measurement_dto, 'application/json')

def measurement_view(request, id):
    if request.method == 'GET':
        measurement = meu.get_measurement(id)
        measurement_dto = serializers.serialize('json', [measurement])
        return HttpResponse(measurement_dto, 'application/json')

    if request.method == 'PUT':
        measurement = meu.update_measurement(id, json.loads(request.body))
        measurement_dto = serializers.serialize('json', [measurement])
        return HttpResponse(measurement_dto, 'application/json')

    if request.method == 'DELETE':
        meu.delete_measurement(id)
        return HttpResponse('Measurement deleted', 'application/json')