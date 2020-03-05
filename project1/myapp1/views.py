from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp1.forms import project1
from myapp1.models import project1


# Create your views here.
def adddata(request):
    if request.method == 'GET':
        form = project1(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/getdata/')
    else:
        form =project1()
    return render(request, 'form.html', {'form': form})


def getdata(request):
    data = Employee.objects.all()
    return render(request, 'show.html', {'data': data})


def delete(request, id):
    # return HttpResponse(id)
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect('/getdata/')


def getdataforedit(request, id):
    data = Employee.objects.get(id=id)
    return render(request, 'editdata.html', {'data': data})

