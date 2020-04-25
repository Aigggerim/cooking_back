from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import status
from rest_framework.response import Response

from api.models import Cook, Recipe
from api.serializers import CookSerializer, RecipeSerializer

@api_view(['GET'])
def cooks(request):
    return Response(CookSerializer(Cook.objects.all(), many=True).data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def recipes(request):
    if request.method == 'GET':
        return Response(RecipeSerializer(Recipe.objects.all(), many=True).data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        pass