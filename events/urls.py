from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),#Aqui é o home do projeto
    path('<int:year>/<str:month>', views.home, name='home'),#Vai para o calendario conforme o mes q se adicione
    path('events/', views.all_events, name="list-events"),#Vai para a pagina q lista todos os eventos
    path('add_venue/', views.add_venue, name="add-venue"),#Vai para pagina de adicao de uma nova venue
    path('list_venues/', views.list_venues, name="list-venues"),#Vai para lista de venues
    path('show_venue/<venue_id>/', views.show_venue, name="show-venue"),#Esse link vai para o venue conforme seu id
    path('search_venues/', views.search_venues, name="search-venues"),#Essa é a parte de pesquisa do projeto
    path('update_venue/<venue_id>/', views.update_venue, name="update-venue"),#Esse link é para o update da Venue conforme seu link
    path('add_event/', views.add_event, name="add-event"),#Essa pagina é para criar um novo evento

]