from django.contrib import admin
from .models import Maktab, Book

class MaktabAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'manzil', 'tashkil_topgan_yili')
    search_fields = ('nomi', 'manzil')


admin.site.register(Maktab, MaktabAdmin)
admin.site.register(Book)