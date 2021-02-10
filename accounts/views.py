from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
  if request.method == 'POST':
    if request.POST['pwd1']==request.POST['pwd2']:
      try:
        user = User.objects.get(username=request.POST['uname'])  #try checked for samename
        return render(request,'accounts/signup.html',{'err_msg':'UserName is already Taken!'})
      except User.DoesNotExist:
        user = User.objects.create_user(username = request.POST['uname'],password = request.POST['pwd2']) # create_user for proper username and password storage
        auth.login(request,user) #logged in
        return redirect('/')
    else:
      return render(request,'accounts/signup.html',{'err_msg':'Password must match!'})
  else:
    return render(request,'accounts/signup.html',{})


def login(request):
  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['uname'],password=request.POST['pwd'])
    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      return render(request,'accounts/login.html',{'err_msg':'User/Password Unknown!'})
  else:
   return render(request,'accounts/login.html',{})



def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('/')