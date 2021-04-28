from django.db import models

class Auto(models.Model):
  registracniZnacka = models.CharField(max_length=100)
  znackaATyp = models.CharField(max_length=100)
  pocetNajetychKm = models.IntegerField()
  datumPosledniTK = models.DateField()


class Zakaznik(models.Model):
  krestniJmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  cisloRidicskehoPrukazu = models.CharField(max_length=40)
  datumNarozeni = models.DateField()

class Vypujcka(models.Model):
  datumVypujcky = models.DateTimeField()
  datumVraceni = models.DateTimeField()
  cena = models.IntegerField()

