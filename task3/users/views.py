# from core.task3.users.models import student
from django.contrib.auth.models import User
from django.contrib.messages.api import info
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username} :) You can now login with your credentials!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def search(request):
    if request.method=="POST":
        srch = request.POST['srh']

        if srch:
            match = User.objects.filter(Q(username__icontains=srch))

            if match:
                return render(request, 'users/searchuser.html', {'sr':match})
            else:
                messages.error(request, 'no result found')

        else:
            return HttpResponseRedirect('/search/')

    return render(request, 'users/searchuser.html')
