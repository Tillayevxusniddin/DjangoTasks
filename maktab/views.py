from django.shortcuts import render, get_object_or_404
from .models import Post, Student


def post_list(request):
    posts = Post.objects.all()  # Barcha postlarni olish
    return render(request, 'post_list.html', {'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def adult_students(request):
    adults = Student.objects.adults()
    return render(request, 'adult_students.html', {'students': adults})