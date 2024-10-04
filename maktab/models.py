from django.db import models

class Maktab(models.Model):
    nomi = models.CharField(max_length=100)
    manzil = models.CharField(max_length=255)
    tashkil_topgan_yili = models.IntegerField()

    def __str__(self):
        return self.nomi
