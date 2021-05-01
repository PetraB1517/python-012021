from django.db import models
from datetime import datetime, timedelta

class Auto(models.Model):
    registracniZnacka = models.CharField(max_length=100)
    znackaATyp = models.CharField(max_length=100)
    pocetNajetychKm = models.IntegerField()
    datumPosledniTK = models.DateField()

    def __str__(self):
        return self.znackaATyp

    @property
    def doTK(self):
        dnesniDatum = datetime.today().date()
        STK = self.datumPosledniTK
        return (dnesniDatum - STK).days


class Zakaznik(models.Model):
    PROGRAM = (
    ('zlaty', 'Zlatý program'),
    ('platinovy', 'Platinový program'),
    ('--', 'Běžný zákazník'))

    krestniJmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    cisloRidicskehoPrukazu = models.CharField(max_length=40)
    datumNarozeni = models.DateField()
    program = models.CharField(max_length=12, choices=PROGRAM)

    def __str__(self):
        return self.krestniJmeno.__str__() + ' ' + self.prijmeni.__str__()

class Vypujcka(models.Model):
  datumVypujcky = models.DateTimeField()
  datumVraceni = models.DateTimeField()
  cena = models.IntegerField()
  auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
  zakaznik = models.ForeignKey(Zakaznik, on_delete=models.SET_NULL, null=True)

  @ property
  def prubeh(self):
    dnesniDatum = datetime.today()
    dnesniDatum = dnesniDatum.date()
    start = self.datumVypujcky.date()
    end = self.datumVraceni.date()

    if start > dnesniDatum:
      return 'Budoucí vypůjčka.'
    elif end < dnesniDatum:
      return 'Již proběhla.'
    else:
      return 'Právě probíhá.'

