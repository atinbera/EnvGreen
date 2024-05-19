from django.shortcuts import render,HttpResponse
from datetime import datetime
from app.models import Contact
from django.contrib import messages
# Create your views here.
def about(request):
    # return HttpResponse("This is the about page")
    return render(request,'about.html')
def index(request):
    # return HttpResponse("Hi, this the page in index")
    context={
        "variable1":"Atin",
        "variable2":"Arya",
    }
    
    return render(request,'index.html',context)

def home(request):
    # return HttpResponse("This is home page")
    return render(request,'home.html')

def contact(request):
    # return HttpResponse("I'm from contact httpresponse")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=
                        datetime.today())
        contact.save()
        messages.success(request, "Message Sent Successfully")
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def pricing(request):
    return render(request,'pricing.html')
# def base(request):
#     return render(request,'home.html')

# python manage.py shell
# from app.models import Contact
# Contact.objects.all()[0].name
# Contact.objects.filter(name="name",phone="99999999")