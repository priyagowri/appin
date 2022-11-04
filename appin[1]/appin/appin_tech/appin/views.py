from django.shortcuts import render
from .models import Datas
# Create your views here.
def home(request):
    return render (request,'app/index.html')
def about(request):
    return render(request,'app/about.html')
def course(request):
    return render(request,'app/course.html')
def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        programs=request.POST["programs"]
        app=Datas()
        app.name=name
        app.email=email
        app.phone=phone
        app.message=message
        app.programs=programs

        app.save()

    return render(request,'app/contact.html')    