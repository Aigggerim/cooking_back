from rest_framework import serializers
from api.models import Recipe, Cook

class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        fields = 'id','name'

class RecipeSerializer(serializers.Serializer):
    mainImage = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = CookSerializer()
    ingredients = serializers.CharField()
    steps = serializers.CharField()
