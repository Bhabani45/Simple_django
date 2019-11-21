from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from CIMIT.forms import VenueForm
from CIMIT.models import Venue

# Create your views here.
def edit(request,id):
    employee = Venue.objects.get(id=id)
    return render(request , "edit.html", {"employee":employee})

def update(request, id):
    employee = Venue.objects.get(id=id)
    form = VenueForm(request.POST , instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/list')
        return render(request , "edit.html", {"employee":employee})

def delete(request , id):
    employee = Venue.objects.get(id=id)
    employee.delete()
    return redirect("/list")

def list(request):
    context = {'list': Venue.objects.all()}
    return render(request , 'list.html' , context)





def add(request ):
    
    if request.method == "POST":
        form = VenueForm(request.POST)
        #form.save()
        if form.is_valid():
            try:
                form.save()
                return redirect('/list')
            except:
                pass
    else :
        form = VenueForm
        return render(request , "add.html" , {"form":form})


