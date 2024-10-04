from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import StudentSignUpForm
from .models import Student

from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book':book})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Yangi studentni ma'lumotlar bazasiga saqlash
            return redirect('student_list')  # Ro'yxatga qaytish
    else:
        form = StudentSignUpForm()
    return render(request, 'student_signup.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


from django.shortcuts import get_object_or_404


def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentSignUpForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentSignUpForm(instance=student)

    return render(request, 'student_edit.html', {'form': form, 'student': student})
