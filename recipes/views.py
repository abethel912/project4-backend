from .models import Recipes
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecipeSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
