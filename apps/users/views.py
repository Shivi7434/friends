from django.shortcuts import render, redirect

from django.contrib import messages
from .models import User 

def home(request):
    return redirect('/')

def main(request):
    return render(request,'users/main.html')

def create(request):
    if request.method == 'POST':
        result =User.objects.validate_registration(request.POST)
        if result['status'] == False:
            for error in result ['errors']:
                 messages.error(request, error)
                 return redirect ('/main')
        else:
            request.session['user_id'] = result ['user'].id
            return redirect('/success')

def success(request):
    return render(request, 'users/friends.html')

def login(request):
    return render(request, 'users/friends.html')

def authenticate(request):
    if request.method == 'POST':
          result = User.objects.validate_login(request.POST)
          if result ['status'] == False:
              messages.error(request, result['error'])
              return redirect('/users/main')
          else:
              
              return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect ('/')      

def profile(request):
    context{
        name={{user.name}}
        email={{user.email}}
    }                  
    return redirect(request,'users/user.html',context)      

       
