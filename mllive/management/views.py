from django.shortcuts import render,redirect
from .models import Taskdb
from .forms import TaskForm
from django.contrib import messages
def home(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items=Taskdb.objects.all()
            messages.success(request,('Task Added  '))
            return render(request,'index.html',{'all_items':all_items})
    else:
        all_items=Taskdb.objects.all()
        return render(request,'index.html',{'all_items':all_items})


    all_items=Taskdb.objects.all()
    return render(request,'index.html',{'all_items':all_items})

def delete(request, list_id):

    task=Taskdb.objects.get(pk=list_id)
    task.delete()
    messages.success(request,('Task deleted'))
    return redirect('home')

# Create your views here.
