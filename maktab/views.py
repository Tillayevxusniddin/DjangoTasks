# views.py
from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm

def upload_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ApplicationForm()
    return render(request, 'upload_form.html', {'form': form})

def index(request):
    applications = Application.objects.all()
    return render(request, 'index.html', {'applications': applications})
