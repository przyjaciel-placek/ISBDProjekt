from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.decorators import api_view, parser_classes

from Pracownik_app.models import Pracownik,Ksiazka,Klient,Zamowienie,Recenzja,Obserwacja
from Pracownik_app.serializers import PracownikSerializer,KsiazkaSerializer,KlientSerializer,ZamowienieSerializer,RecenzjaSerializer,ObserwacjaSerializer


# Create your views here.


@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def getSixNewestBooksApi(request):
    if request.method=='GET':
        ksiazka = Ksiazka.objects.all()
        ksiazka_serializer = KsiazkaSerializer(ksiazka[:6],many=True)
        return JsonResponse(ksiazka_serializer.data,safe=False)


@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def ksiazkaApi(request,id=0):
    if request.method=='GET':
        ksiazka = Ksiazka.objects.all()
        ksiazka_serializer = KsiazkaSerializer(ksiazka,many=True)
        return JsonResponse(ksiazka_serializer.data,safe=False)
    elif request.method=='POST':
        ksiazka_data = request.data
        pracownik = Pracownik.objects.get(pk=ksiazka_data['DodalIdP'])
        ksiazka_data['DodalIdP'] = pracownik.pk
        ksiazka_serializer = KsiazkaSerializer(data=ksiazka_data)
        if ksiazka_serializer.is_valid():
            ksiazka_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(ksiazka_serializer.errors)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        ksiazka_data = request.data
        ksiazka = Ksiazka.objects.get(ISBN=ksiazka_data['ISBN'])
        ksiazka_serializer = KsiazkaSerializer(ksiazka, data = ksiazka_data)
        if ksiazka_serializer.is_valid():
            ksiazka_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        ksiazka=Ksiazka.objects.get(ISBN=id)
        ksiazka.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def klientApi(request,id=0):
    if request.method=='GET':
        klient = Klient.objects.all()
        klient_serializer = KlientSerializer(klient,many=True)
        return JsonResponse(klient_serializer.data,safe=False)
    elif request.method=='POST':
        klient_data = request.data
        klient_serializer = KlientSerializer(data=klient_data)
        if klient_serializer.is_valid():
            klient_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(klient_serializer.errors)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        klient_data = request.data
        klient = Klient.objects.get(pk=klient_data['IdK'])
        klient_serializer = KlientSerializer(klient, data = klient_data)
        if klient_serializer.is_valid():
            klient_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        klient=Klient.objects.get(pk=id)
        klient.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def pracownikApi(request,id=0):
    if request.method=='GET':
        pracownik = Pracownik.objects.all()
        pracownik_serializer = PracownikSerializer(pracownik,many=True)
        return JsonResponse(pracownik_serializer.data,safe=False)
    elif request.method=='POST':
        pracownik_data = request.data
        pracownik_serializer = PracownikSerializer(data=pracownik_data)
        if pracownik_serializer.is_valid():
            pracownik_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(pracownik_serializer.errors)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        pracownik_data = request.data
        pracownik = Pracownik.objects.get(pk=pracownik_data['IdP'])
        pracownik_serializer = PracownikSerializer(pracownik, data = pracownik_data)
        if pracownik_serializer.is_valid():
            pracownik_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        pracownik=Pracownik.objects.get(pk=id)
        pracownik.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def zamowienieApi(request,id=0):
    if request.method=='GET':
        zamowienie = Zamowienie.objects.all()
        zamowienie_serializer = ZamowienieSerializer(zamowienie,many=True)
        return JsonResponse(zamowienie_serializer.data,safe=False)
    elif request.method=='POST':
        zamowienie_data = request.data
        LoginK = Klient.objects.get(pk=zamowienie_data['LoginK'])
        IdKs = Ksiazka.objects.get(pk=zamowienie_data['IdKs'])
        zamowienie_data['LoginK'] = LoginK.pk
        zamowienie_data['IdKs'] = IdKs.pk
        zamowienie_serializer = ZamowienieSerializer(data=zamowienie_data)
        if zamowienie_serializer.is_valid():
            zamowienie_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(zamowienie_serializer.errors)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        zamowienie_data = request.data
        zamowienie = Zamowienie.objects.get(pk=zamowienie_data['IdZ'])
        zamowienie_serializer = ZamowienieSerializer(zamowienie, data = zamowienie_data)
        if zamowienie_serializer.is_valid():
            zamowienie_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        zamowienie=Zamowienie.objects.get(pk=id)
        zamowienie.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def recenzjaApi(request,id=0):
    if request.method=='GET':
        recenzja = Recenzja.objects.all()
        recenzja_serializer = RecenzjaSerializer(recenzja,many=True)
        return JsonResponse(recenzja_serializer.data,safe=False)
    elif request.method=='POST':
        recenzja_data = request.data
        LoginK = Klient.objects.get(pk=recenzja_data['LoginK'])
        IdKs = Ksiazka.objects.get(pk=recenzja_data['IdKs'])
        recenzja_data['LoginK'] = LoginK.pk
        recenzja_data['IdKs'] = IdKs.pk
        recenzja_serializer = RecenzjaSerializer(data=recenzja_data)
        if recenzja_serializer.is_valid():
            recenzja_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(recenzja_serializer.errors)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        recenzja_data = request.data
        recenzja = Recenzja.objects.get(pk=recenzja_data['IdR'])
        recenzja_serializer = RecenzjaSerializer(recenzja, data = recenzja_data)
        if recenzja_serializer.is_valid():
            recenzja_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        recenzja=Recenzja.objects.get(pk=id)
        recenzja.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@parser_classes([JSONParser])
def obserwacjaApi(request,id=0):
    if request.method=='GET':
        obserwacja = Obserwacja.objects.all()
        obserwacja_serializer = ObserwacjaSerializer(obserwacja,many=True)
        return JsonResponse(obserwacja_serializer.data,safe=False)
    elif request.method=='POST':
        obserwacja_data = request.data
        LoginK = Klient.objects.get(pk=obserwacja_data['LoginK'])
        IdKs = Ksiazka.objects.get(pk=obserwacja_data['IdKs'])
        obserwacja_data['LoginK'] = LoginK.pk
        obserwacja_data['IdKs'] = IdKs.pk
        obserwacja_serializer = ObserwacjaSerializer(data=obserwacja_data)
        if obserwacja_serializer.is_valid():
            obserwacja_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(obserwacja_serializer.errors)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        obserwacja_data = request.data
        obserwacja = Obserwacja.objects.get(pk=obserwacja_data['IdO'])
        obserwacja_serializer = ObserwacjaSerializer(obserwacja, data = obserwacja_data)
        if obserwacja_serializer.is_valid():
            obserwacja_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        obserwacja=Obserwacja.objects.get(pk=id)
        obserwacja.delete()
        return JsonResponse("Deleted Successfully", safe=False)