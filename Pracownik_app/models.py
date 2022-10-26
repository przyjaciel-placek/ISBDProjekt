from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Pracownik(models.Model):
    LoginP = models.CharField(primary_key=True, max_length=20)
    ImieP = models.CharField(max_length=30)
    NazwiskoP = models.CharField(max_length=30)
    PeselP = models.CharField(max_length=11)
    
