from rest_framework import serializers
from api.models import Recipe, Cook, Comment, Manager

class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        fields = 'id','name'
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = 'id','username'

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    mainImage = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = CookSerializer()
    ingredients = serializers.CharField()
    steps = serializers.CharField()

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    commentData = serializers.CharField()
    recipe = RecipeSerializer()