from rest_framework.views import APIView
from rest_framework.response import Response
from RecipeBackend.models import Recipe
import random
import json

class HelloWorld(APIView):
    def get(self,request):
        return Response("Hello World")
        

class RandomRecipe(APIView):
    def get(self,request):
        resp_dict = {
            'status': None,
            'message': None,
            'data': None
        }
        try:
            size = Recipe.objects.filter().count()
            id = random.randint(1,size)
            recipe = Recipe.objects.filter(id=id).first()
            print(recipe.name)
            data = {
                'name':recipe.name,
                'category':recipe.category,
                'region':recipe.region,
                'ingredients':[val.split(',') for val in recipe.ingredients.split(":")],
                'instructions':[val for val in recipe.instructions.split('\r\n')],
                'imageURL':recipe.imageURL
            }
            resp_dict['status'] = "success"
            resp_dict['data'] = json.dumps(data)
            resp = Response(resp_dict)
            resp.status_code = 200
        except:
            resp_dict['status'] = "failed"
            resp_dict['data'] = None
            resp = Response(resp_dict)
            resp.status_code = 500
        return resp

# Create your views here.
