from django.shortcuts import render

def home(request):
    student_image_url = '/media/students/student2.jpg'
    return render(request, 'home.html', {'student_image_url': student_image_url})
