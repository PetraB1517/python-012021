from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView

from . import models


class IndexView(View):
  def get(self, request):
    return HttpResponse(
      """<h1>Vítejte na stránkách naší autopůjčovny!</h1>
      <a href='http://localhost:8000/katalog/seznam/'>Katalog našich aut >> </a><br>
      <h2>O naší autopůjčovně</h2>
      <p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
      <h2> Kde nás najdete?</h2>
      <p>Pro nacházíme se  na adrese Babišova 666, Zemanov 123 45</p2>
      <h2>Kontakty</h2>
      <ul style='list-style-type:none'>
        <li> <a href='https://facebook.com'>Facebook</a> </li>
        <li> +420 666 666 666 </li>
        <li> babisova.autopujcovna@kriminalnici.cz </li>
      </ul>
      """)


class SeznamView(ListView):
    #def get(self, request):
    # return HttpResponse("Zde bude seznam aut.")
    model = models.Auto
    template_name = "katalog/seznam_aut.html"


class VypujckaView(ListView):
    model = models.Vypujcka
    template_name = "katalog/vypujcky_list.html"


class ZakazniciView(ListView):
    model = models.Zakaznik
    template_name = "katalog/zakaznici_list.html"