from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import LoginUserForm, NewUserForm


def user_login(request):
    if request.user.is_authenticated and 'next' in request.GET:
        messages.add_message(request, messages.ERROR, 'Yetkiniz yok!.')
        return render(request, 'account/login.html')
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                messages.add_message(request, messages.SUCCESS, 'Başarılı bir şekilde giriş yaptınız.')
                nextUrl = request.GET.get('next', None)
                if nextUrl is None:
                    return redirect('index')
                else:
                    return redirect(nextUrl)
            else:
                return render(request, 'account/login.html', {'form': form})
        else:
            return render(request, 'account/login.html', {'form': form})
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/register.html', {'form': form,})
        
    else:
        form = NewUserForm()
        return render(request, 'account/register.html', {'form': form,})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Başarılı bir şekilde çıkış yaptınız.')
    return redirect("index")
