from django.shortcuts import render,HttpResponse

from home.models import Contact
# Create your views here.
def home(request):
    content={"Name":"VAMSI KRISHNA",
             "Course":"Django"}
    #return HttpResponse("This is Home Page")
    return render(request,"home.html",content)
def about(request):
    
    return render(request,"about.html")
def projects(request):
    
    return render(request,"projects.html")
def contact(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        phone=request.POST['Phone']
        message=request.POST['Message']
        ins=Contact(name=name,email=email,phone=phone,message=message)
        ins.save()
        print("Data has been written to database")

        #print(name, email, phone, message)
    
    return render(request,"contact.html")

