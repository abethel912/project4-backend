from .models import Recipes
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Recipes
        # the fields that should be included in the serialized output
        fields = ['name', 'img', 'cuisine', 'ingredients', 'directions', 'time']
