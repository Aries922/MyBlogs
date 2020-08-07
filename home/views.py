from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Feed
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def home(request):
    allfeeds=Feed.objects.all()
    context={'allfeeds':allfeeds}
    return render(request,"home/home.html",context)

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        textarea=request.POST['textarea']

        if len(name)<3 or len(email)<5 or len(phone)<=9 or len(textarea)<10:
            messages.error(request,'Please fill the Form Correctly')
        else:
            contact=Contact(name=name,email=email,phone=phone,textarea=textarea)
            contact.save()
            messages.success(request,'Your Message is Sent to Admin')
    return render(request,"home/contact.html")    
    
 

def about(request):
    return render(request,"home/about.html")

def search(request):
    query=request.GET['query']
    if len(query)>150:
        messages.error(request,'no search resluts found')

    else:
        allfeedsheading=Feed.objects.filter(heading__icontains=query)
        allfeedscontent=Feed.objects.filter(content__icontains=query)
        allfeeds=allfeedsheading.union(allfeedscontent)
    params={'allfeeds':allfeeds}
    
    return render(request,'home/search.html',params)    


def signup(request):

    if request.method == 'POST':
        fname=request.POST['fname']
        sname=request.POST['sname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"please enter less than 10 character")
            return redirect('home') 

        if pass1 !=pass2 :
            messages.error(request,"both passwords must be same")
            return redirect('home')

               
        user = User.objects.create_user(username=username,password=pass1,email=email,first_name=fname,last_name=sname)
        user.save()
        messages.success(request,"your account is created")
        return redirect("home")

    else:
        return HttpResponse("404 Error Not Found")


def login(request):

     if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)
        

        if user is not None:
            auth_login(request,user)
            messages.success(request,'SUccessfully logged in')
            return redirect("home")
        else:
            messages.error(request, 'please Check your credentials')
            return redirect("home")    

    
    

def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")
