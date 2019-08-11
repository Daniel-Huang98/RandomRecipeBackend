"""RecipeBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .RecipeAPI import views
import json
from .models import Recipe

syncBool = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test',views.HelloWorld.as_view()),
    path('randomrecipe', views.RandomRecipe.as_view())
]

def sync():
    a = open("updatedData.txt", "r")
    while(True):
        try:
            data = json.loads(a.readline())
            recipe = Recipe()
            recipe.name = data['name']
            recipe.category = data['category']
            recipe.region = data['region']
            recipe.ingredients = data['ingredients']
            recipe.instructions = data['instructions']
            recipe.imageURL = data['imageURL']
            recipe.save()
            print("Loaded: ", data['name'])
        except Exception as e:
            print(e)
            break
    print('loaded data')
    
if(syncBool):
    sync()