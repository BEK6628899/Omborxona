from django.db import models
from django.contrib.auth.models import User

class Ombor(models.Model):
    nom = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    tel = models.CharField(max_length=15)
    ism = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=30)
    narx = models.SmallIntegerField()
    berilgan_sana = models.DateField()
    miqdori = models.SmallIntegerField()
    olchov = models.TextField()
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Client(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    qarz = models.SmallIntegerField()
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism


