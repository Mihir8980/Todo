from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import todoSerializer

# Create your views here.
def home(request):
    list_of_todo = Todo.objects.all().order_by("added_date")
    return render(request,'main/index.html',{
        "list_of_todo":list_of_todo
    })

@csrf_exempt
def add_to_do(request):
    added_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(text=content,added_date=added_date)
    return HttpResponseRedirect('/')

def delete_to_do(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

'''def imp(request,i):
    Todo.flag=True:
    return HttpResponse('/')'''
    
class todoList(APIView):
    def get(self,request):
        todo_list = Todo.objects.all()
        serializers = todoSerializer(todo_list, many=True)
        return Response(serializers.data)

    def post(self):
        pass