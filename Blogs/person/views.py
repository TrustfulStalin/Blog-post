from django.shortcuts import render
## For sending JSON Responses
from django.http import JsonResponse
## To serialize objects into json strings
from django.core.serializers import serialize
## To turn json strings into dictionaries
import json
## The Turtle Model
from .models import User
## View class
from django.views import View
## GetBody
from .helpers import GetBody


class UserView(View):
    
    def get(self, request):
     
        all = User.objects.all()
        ## Turn the object into a json string
        serialized = serialize("json", all)
        ## Turn the json string into a dictionary
        finalData = json.loads(serialized)
        ## Send json response, turn safe off to avoid errors
        return JsonResponse(finalData, safe=False)


    def post (self, request):
        ## get data from the body
        body = GetBody(request)
        print(body)
        
        user = User.objects.create(title=body["title"], body=body["body"])
       
        finalData = json.loads(serialize("json", [user])) 
        ## Send json response
        return JsonResponse(finalData, safe=False)
    
class UserViewID(View):
    
    def get (self, request, id):
        
        user = User.objects.get(id=id)
       
        finalData = json.loads(serialize("json", [user]))
    
        return JsonResponse(finalData, safe=False)
   
    def put (self, request, id):
        ## get the body
        body = GetBody(request)
        
        ## ** is like JS spread operator
        User.objects.filter(id=id).update(**body)
        ## query for turtle
        user = User.objects.get(id=id)
        ## serialize and make dict
        finalData = json.loads(serialize("json", [user]))
        ## return json data
        return JsonResponse(finalData, safe=False)

    def delete (self, request, id):
    
        user = User.objects.get(id=id)
        
        user.delete()
    
        finalData = json.loads(serialize("json", [user]))
        ##send json response
        return JsonResponse(finalData, safe=False)

# Create your views here.
