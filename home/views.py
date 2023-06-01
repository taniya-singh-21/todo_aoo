from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import todo

# Create your views here.

def index(request):
    list_todo = todo.objects.filter(status=False)
    return render(request,'base.html',{'list_todo':list_todo})

def mark_as_done(request,id):
    obj=todo.objects.get(pk = id)
    obj.status=True
    obj.save()
    list_todo = todo.objects.filter(status=False)
    return render(request,'base.html',{'list_todo':list_todo})


def new_todo(request):
    if request.method == "POST":
        todo.objects.create(name=request.POST.get('todo-name'))
        list_todo = todo.objects.filter(status =False)
        return render(request,'base.html',{'list_todo':list_todo})

def deleteCompleted(request):
    todo.objects.filter(status=True).delete()
    return render(request,'base.html')

def deleteall (request):
    todo.objects.all().delete()
    return render(request,'base.html')