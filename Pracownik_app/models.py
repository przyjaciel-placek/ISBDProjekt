from django.db import models

class Pracownik(models.Model):
    IdP = models.AutoField(primary_key=True)
    LoginP = models.CharField(max_length=20)
    ImieP = models.CharField(max_length=30)
    NazwiskoP = models.CharField(max_length=30)
    PeselP = models.CharField(max_length=11)
    DataZatr = models.DateField()                                  
    HasloP = models.CharField(max_length=64)
    
class Klient(models.Model):
    IdK = models.AutoField(primary_key=True)
    LoginK = models.CharField(max_length=20)
    ImieK = models.CharField(max_length=30)
    NazwiskoK = models.CharField(max_length=30)
    HasloK = models.CharField(max_length=64)
    AdresK = models.CharField(max_length=80)

class Ksiazka(models.Model):                                       
    ISBN = models.CharField(primary_key=True, max_length=17)
    TytulKs = models.CharField(max_length=150)
    AutorKs = models.CharField(max_length=255)
    CenaKs = models.FloatField()
    Ilosc = models.IntegerField()
    DodalIdP = models.ForeignKey(Pracownik, on_delete=models.DO_NOTHING)

class Zamowienie(models.Model):
    IdZ = models.AutoField(primary_key=True)            
    DataZ = models.DateField()                                      
    Status = models.CharField(max_length=30)
    LoginK = models.ForeignKey(Klient, on_delete=models.DO_NOTHING)                                         
    IdKs = models.ForeignKey(Ksiazka, on_delete=models.DO_NOTHING)                                            

class Recenzja(models.Model):
    IdR = models.IntegerField(primary_key=True)
    TrescR = models.CharField(max_length=2000)
    DataWyst = models.DateField()
    LoginK = models.ForeignKey(Klient, on_delete=models.DO_NOTHING) 
    IdKs = models.ForeignKey(Ksiazka, on_delete=models.DO_NOTHING)
    Ocena = models.FloatField()

class Obserwacja(models.Model):
    IdO = models.PositiveIntegerField(primary_key=True)
    LoginK = models.ForeignKey(Klient, on_delete=models.DO_NOTHING) 
    IdKs = models.ForeignKey(Ksiazka, on_delete=models.DO_NOTHING)