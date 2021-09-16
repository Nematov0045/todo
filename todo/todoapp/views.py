from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Todo
# Create your views here.
#получение баз данных
def homepage(request):
    todos=Todo.objects.all()
    return render(request,'index.html',{'todos':todos})
    #сохранение баз данных
def create(request):
    if request.method == 'POST':
        todo= Todo()
        todo.title=request.POST.get('title')
        todo.description=request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')
#изменение даных из БД
def edit(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if request.method=='POST':
            todo.title=request.POST.get('title')
            todo.description=request.POST.get('description')
            todo.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'edit.html',{'todo':todo})
    except Todo.DoesNotExist:
        return HttpResponseNotFound
        ("<h2>задача не найдена</h2>")