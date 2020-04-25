from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import status, APIView
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
        try:
            author = Cook.objects.get(name=request.data['author'])
        except:
            author = Cook.objects.create(
                name = request.data['author']
            )
        Recipe.objects.create(
            author = author,
            title = request.data['name'],
            description = request.data['description'],
            ingredients = request.data['ingredients'],
            mainImage = request.data['image'],
            steps = request.data['steps'],
        )
        return Response({"recipe": "created"}, status=status.HTTP_201_CREATED)

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

class RecipeUpdateView(APIView):
    def put(self, request, id):
        recipe = Recipe.objects.get(id=request.data['id'])
        
        recipe.title = request.data['name']
        recipe.description = request.data['description']
        recipe.ingredients = request.data['ingredients']
        recipe.mainImage = request.data['image']
        recipe.steps = request.data['steps']
        recipe.save()
        return Response({"recipe":"updated"}, status=status.HTTP_200_OK)

class RecipeDeleteView(APIView):
    def delete(self, request, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return Response({"recipe":"deleted"}, status=status.HTTP_200_OK)
