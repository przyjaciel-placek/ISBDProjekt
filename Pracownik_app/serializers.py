from rest_framework import serializers
from Pracownik_app.models import Pracownik,Ksiazka,Klient,Zamowienie,Recenzja,Obserwacja

class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pracownik
        fields=('IdP','LoginP','ImieP','NazwiskoP','PeselP','DataZatr','HasloP')

class KsiazkaSerializer(serializers.ModelSerializer):
    DodalIdP = serializers.PrimaryKeyRelatedField(queryset=Pracownik.objects.all())

    class Meta:
        model=Ksiazka
        fields=('ISBN','TytulKs','AutorKs','CenaKs','DodalIdP')

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Klient
        fields=('IdK','LoginK','ImieK','NazwiskoK','HasloK','AdresK')
        
class ZamowienieSerializer(serializers.ModelSerializer):
    LoginK = serializers.PrimaryKeyRelatedField(queryset=Klient.objects.all())
    IdKs = serializers.PrimaryKeyRelatedField(queryset=Ksiazka.objects.all())

    class Meta:
        model=Zamowienie
        fields=('IdZ','DataZ','Status','LoginK','IdKs')

class RecenzjaSerializer(serializers.ModelSerializer):
    LoginK = serializers.PrimaryKeyRelatedField(queryset=Klient.objects.all())
    IdKs = serializers.PrimaryKeyRelatedField(queryset=Ksiazka.objects.all())
    class Meta:
        model=Recenzja
        fields=('IdR','TrescR','DataWyst','LoginK','IdKs')

class ObserwacjaSerializer(serializers.ModelSerializer):
    LoginK = serializers.PrimaryKeyRelatedField(queryset=Klient.objects.all())
    IdKs = serializers.PrimaryKeyRelatedField(queryset=Ksiazka.objects.all())
    class Meta:
        model=Obserwacja
        fields=('IdO','LoginK','IdKs')

