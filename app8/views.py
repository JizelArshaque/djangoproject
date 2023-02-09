from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm,UpdateForm,ChangePassword
from . models import Register,Gallery
from django.contrib import messages
from django.contrib.auth import logout as logouts
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            photo=form.cleaned_data['Photo']
        user=Register.objects.filter(Email=email)
        if user:
            messages.warning(request,"already")
            return redirect('/register')
        elif password!=confirmpassword:
            messages.warning(request,"mismatch")
            return redirect('register')
        else:
            tab=Register(Name=name,Age=age,Place=place,Email=email,Password=password,Photo=photo)
            tab.save()
            messages.success(request,"success")
            return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
def login(request):
    if request.method=='POST':
     form=LoginForm(request.POST)
     if form.is_valid():
        email=form.cleaned_data['Email']
        password=form.cleaned_data['Password']

     try:
        user=Register.objects.get(Email=email)
        if not user:
            messages.warning(request,"Does not exists")
            return redirect('/login')
        elif password!=user.Password:
            messages.warning(request,"Incorrect password")
            return redirect('/login')
        else:
            messages.success(request,"success")
            return redirect('/home/%s'%user.id)
     except:
         messages.warning(request,"Username or Password incorrect")
         return redirect('/login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request,id):
    data=Register.objects.get(id=id)
    return render(request,'home.html',{'data':data})

def update(request,id):
    data=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"SUCCESS!!")
            return redirect('/')
    else:
        form=UpdateForm(instance=data)
    return render(request,'update.html',{'data':data,'form':form})


def logout(request):
    logouts(request)
    messages.success(request,"Logged out!")
    return redirect('/')

def changepassword(request,id):
    data=Register.objects.get(id=id)
    if request.method=='POST':
        form=ChangePassword(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=data.Password:
                messages.warning(request,"Incorrect passowrd!!")
                return redirect('/changepassword/%s' % data.id)
            elif oldpassword==newpassword:
                messages.warning(request,"older and new passwords are same! choose another password!!")
                return redirect('/changepassword/%s' % data.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"mismatch")
                return redirect('/changepassword/%s' % data.id)
            else:
                data.Password=newpassword
                data.save()
                messages.success(request,"success")
            return redirect('/')
    else:
        form=ChangePassword()
    return render(request,'changepassword.html',{'form':form})

def gallery(request):
    data=Gallery.objects.all()
    return render(request,'gallery.html', {'data':data})
def pic1(request,id):
    data=Gallery.objects.get(id=id)
    return render(request,'pic1.html', {'data':data})

