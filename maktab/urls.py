from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # path('posts/', views.post_list, name='post_list'),  # Postlar ro'yxati uchun yo'nalish
                  # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  # Har bir post uchun detal sahifa
                  # path('adult_students/', views.adult_students, name='adult_students'),

                  # path('login/', views.user_login, name='login'),
                  # path('profile/', views.profile, name='profile'),
                  # path('logout/', views.user_logout, name='logout'),
                  # path('signup/', views.signup_view, name='signup')
                  path('home/', views.home, name='home'),

              ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
