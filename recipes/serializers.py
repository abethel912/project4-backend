from .models import Recipes
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id','name', 'img', 'cuisine', 'ingredients', 'directions', 'time']
