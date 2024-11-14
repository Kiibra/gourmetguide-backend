from gourmetguide.models import Recipe
from gourmetguide.serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def recipes(request):
    data = Recipe.objects.all()
    serializer = RecipeSerializer(data, many=True)
    return Response({'recipes': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Recipe added successfully!', 'recipes': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recipe_detail(request, recipe_id):  # Use recipe_id here (lowercase 'i')
    recipe = get_object_or_404(Recipe, id=recipe_id)
    serializer = RecipeSerializer(recipe)
    return Response({'recipe': serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def recipe_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Recipe updated successfully!', 'recipes': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return Response({'message': 'Recipe deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
