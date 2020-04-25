from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import status
from rest_framework.response import Response

from api.models import Cook, Recipe, Comment
from api.serializers import CookSerializer, RecipeSerializer, CommentSerializer

@api_view(['GET'])
def cooks(request):
    return Response(CookSerializer(Cook.objects.all(), many=True).data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def recipes(request):
    if request.method == 'GET':
        return Response(RecipeSerializer(Recipe.objects.all(), many=True).data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        pass

@api_view(['GET', 'POST'])
def comments(request):
    if request.method == 'GET':
        return Response(CommentSerializer(Comment.objects.all(), many=True).data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        recipe = Recipe.objects.get(id=request.data['id'])
        Comment.objects.create(
            recipe = recipe,
            username = request.data['name'],
            commentData = request.data['text']
        )
        return Response({"comments status": "posted"}, status=status.HTTP_201_CREATED)