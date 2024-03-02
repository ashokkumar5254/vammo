from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import userform,profile_form,user_form
from .models import profile
from django.contrib.auth.models import User
from productapp.models import category,product
# Create your views here.
def signup(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,'signup.html',{'form':form})
def home(request):
    data1=category.objects.all()
    data2=data1.count()
    return render(request,'home.html',{'data1':data1,'data2':data2})
def profile_view(request):
    try:
        ashok=profile.objects.get(user=request.user)
    except profile.DoesNotExist:
        ashok=profile.objects.create(user=request.user)

    return render(request,'profile.html',{'ashok':ashok})
def edit_profile(request):
    if request.method=='POST':
        form1=profile_form(request.POST,request.FILES,instance=request.user.profile)
        form2=user_form(request.POST,instance=request.user)
        if  form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('profile')
        else:
            return HttpResponse('give proper input')
    data1=profile_form(instance=request.user.profile)
    data2=user_form(instance=request.user)
    return render(request,'edit_profile.html',{'data1':data1,'data2':data2})