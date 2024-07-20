from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from ..forms import RegisterForm  

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
