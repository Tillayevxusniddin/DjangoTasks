from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Siz tizimga muvaffaqiyatli kirdingiz')
            return redirect('profile')  # Profile sahifasiga yo'naltirish
        else:
            messages.error(request, 'Login yoki parol xato')
            return redirect('login')  # Login sahifasiga qaytarish
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.info(request, 'Siz tizimdan chiqib ketdingiz')
    return redirect('login')  # Login sahifasiga qaytarish


@login_required
def profile(request):
    return render(request, 'profile.html')
