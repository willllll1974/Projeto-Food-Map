from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .mongo import comidas_collection


def listar_comidas(request):
    comidas = []

    for comida in comidas_collection.find():
        comida["_id"] = str(comida["_id"])
        comidas.append(comida)

    return JsonResponse(comidas, safe=False)