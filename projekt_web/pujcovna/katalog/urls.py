from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('seznam/', views.SeznamView.as_view(), name='seznamaut'),
  path('vypujcky/', views.VypujckaView.as_view(), name='vypujcky'),
  path('zakaznici/', views.ZakazniciView.as_view(), name='seznam_zakazniku'),
]