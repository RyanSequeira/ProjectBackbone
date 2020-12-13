from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('company/', views.company, name='blog-company'),
    path('DirtyJane\'sAntiques/', views.dja, name='DirtyJane\'sAntiques'),
    path('2SquaresADay/', views.twosq, name ='2SquaresADay'),
    path('SouthsideAntiques,LLC', views.southside_antiques, name = 'SouthsideAntiques,LLC'),
    path('AntiqueStores/', views.antique_stores, name ='AntiqueStores'),
    path('Villy\'s/', views.villys, name ='Villy\'s'),
    path('FatCats/', views.fat_cats, name ='FatCats'),
    path('AtlantaVintageBooks/', views.avb, name ='AVB'),
    path('CalicoCatBookshop/', views.calico, name ='Calico'),
    path('Restaurants/', views.restaurants, name='Restaurants'),
    path('Bookstores/', views.bookstores, name = 'Bookstores')
]

#Boop
#Beep
