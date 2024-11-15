"""
URL configuration for gourmetguide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gourmetguide import views

urlpatterns = [
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/addrecipe/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:recipe_id>/update/', views.recipe_update, name='update_recipe'),
    path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='delete_recipe'),
]
