from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),  # Postlar ro'yxati uchun yo'nalish
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  # Har bir post uchun detal sahifa
    path('adult_students/', views.adult_students, name='adult_students'),
]
