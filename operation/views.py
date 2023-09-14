from django.shortcuts import render,redirect
from . models import Crud
def index (request):
    crud=Crud.objects.all()
    context={
        'crud':crud,
    }
    return render(request,'index.html',context)
def add (request):
    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST.get('dept')
        salary=request.POST['salary']
        # print(name,dept,salary)
        crud=Crud(
            name=name,
            dept=dept,
            salary=salary
        )
        crud.save()
        return redirect('/index')
    return render(request,'add.html')

def update(request,pk):
    update=Crud.objects.get(id=pk)
    if request. method == "POST":
        name=request.POST['name']
        dept=request.POST['dept']
        salary=request.POST['salary']
        update.name=name
        update.dept=dept
        update.salary=salary
        update.save()
        return redirect('/index')

    return render(request,'update.html')
def delete(request,pk):
    curd=Crud.objects.get(id=pk)
    curd.delete()
    return redirect('/index')

# Create your views here.
