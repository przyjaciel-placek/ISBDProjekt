from django.conf.urls import url
from Pracownik_app import views


urlpatterns = [

    url(r'newest/',views.getSixNewestBooksApi),


    url(r'^ksiazka$',views.ksiazkaApi),
    url(r'^ksiazka/([0-9]+)$',views.ksiazkaApi),

    url(r'^klient$',views.klientApi),
    url(r'^klient/([0-9]+)$',views.klientApi),

    url(r'^pracownik$',views.pracownikApi),
    url(r'^pracownik/([0-9]+)$',views.pracownikApi),

    url(r'^zamowienie$',views.zamowienieApi),
    url(r'^zamowienie/([0-9]+)$',views.zamowienieApi),

    url(r'^recenzja$',views.recenzjaApi),
    url(r'^recenzja/([0-9]+)$',views.recenzjaApi),

    url(r'^obserwacja$',views.obserwacjaApi),
    url(r'^obserwacja/([0-9]+)$',views.obserwacjaApi)
]
