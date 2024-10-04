from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('signup/', views.student_signup, name='student_signup'),
    path('students/', views.student_list, name='student_list'),
    path('students/edit/<int:student_id>/', views.student_edit, name='student_edit'),
]