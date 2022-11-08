from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Pracownik(models.Model):
    LoginP = models.CharField(primary_key=True, max_length=20)
    ImieP = models.CharField(max_length=30)
    NazwiskoP = models.CharField(max_length=30)
    PeselP = models.CharField(max_length=11)
    DataZatr = models.DateField()                                   # argumenty??
    HasloP = models.CharField(max_length=64)
    
class Klient(models.Model):
    LoginK = models.CharField(primary_key=True, max_length=20)
    ImieK = models.CharField(max_length=30)
    NazwiskoK = models.CharField(max_length=30)
    HasloK = models.CharField(max_length=64)
    AdresK = models.CharField(max_length=80)

class Ksiazka(models.Model):                                        # ???
    IdKs = models.PositiveIntegerField(primary_key=True)
    TytulKs = models.CharField(max_length=150)
    AutorKs = models.CharField(max_length=255)
    CenaKs = models.FloatField()

class Zamowienie(models.Model):
    IdZ = models.PositiveIntegerField(primary_key=True)             # autonumeracja do dodania
    DataZ = models.DateField()                                      # argumenty??
    Status = models.CharField(max_length=30)
    LoginK = Klient.LoginK                                          # ???????
    IdKs = Ksiazka.IdKs                                             # ???????

class Recenzja(models.Model):
    IdR = models.IntegerField(primary_key=True)
    TrescR = models.CharField(max_length=2000)
    DataWyst = models.DateField()
    LoginK = Klient.LoginK
    IdKs = models.IntegerField()

class Obserwacja(models.Model):
    IdO = models.PositiveIntegerField(primary_key=True)
    LoginK = Klient.LoginK
    IdKs = Ksiazka.IdKs
