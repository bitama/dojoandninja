from django.shortcuts import render,redirect
from.models import Dojo,Ninja

def index(request):
    context={
        "all_dojos":Dojo.objects.all()
    }
    return render(request,"index.html" ,context)

def dojos_create(request):
    Dojo.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"]
    )
    return redirect("/")
def ninjas_create(request):
    Ninja.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        dojo=Dojo.objects.get(id=request.POST["dojo_id"])
        
    )
    return redirect("/")

def dojos_delete(request,dojos_id):
    Dojo.objects.get(id=dojos_id).delete()
    return redirect("/")
    
