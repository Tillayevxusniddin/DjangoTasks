from django.contrib import admin

from maktab.models import Post, Student, Course

# from .models import Maktab, Book

# class MaktabAdmin(admin.ModelAdmin):
#     list_display = ('nomi', 'manzil', 'tashkil_topgan_yili')
#     search_fields = ('nomi', 'manzil')


# admin.site.register(Maktab, MaktabAdmin)
# admin.site.register(Book)

admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Course)