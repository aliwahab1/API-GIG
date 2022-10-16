import email
from gzip import FNAME
# import logging
# from pipes import Template
# from re import template
from urllib import request
# from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

import authentication

# Create your views here.
# def home(request):
#     return HttpResponse('hello I am Ali Wahab')

# def home(rquest):
#     return render(request, "authentication/index.html")

def home(request):
    context = locals()
    templates = 'authentication/index.html'
    return render(request,templates,context)


# def signup(request):

#     if request.method == "POST":
#         # username = request.POST.get('username')
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.lirst_name = lname
#         myuser.save()

#         messages.success(request, "Your Account has been Successfully created.")
#         return redirect('signin')


#     context = locals()
#     templates = 'authentication/index.html'
#     return render(request,templates,context)





def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.lirst_name = lname
        myuser.save()

        messages.success(request, "Your Account has been Successfully created.")
        return redirect('signin') 

    return render(request, "authentication/signup.html")


# def signin(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authentication(username=username, password=pass1)

#         if user is not None:
#             logging(request, user)
#             fname = user.first_name
#             return render(request, "authentication/signin.html", {'fname': fname})

#         else:
#             messages.error(request, "Bad Credentials!")
#             return redirect('home')


#     context = locals()
#     templates = 'authentication/index.html'
#     return render(request,templates,context)



def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authentication(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # fname = user.first_name
            return render(request, "authentication/signin.html", {'fname': FNAME})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
        
    return render(request, "authentication/signin.html")

def signout(request):
    pass