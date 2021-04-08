"""Histogram platů
Stáhni si znovu soubor platy_2021_02.csv s informacemi o platech v softwarové firmě,
se kterými jsme již pracovali v příkladu 26.

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins),
aby byl graf přehledný a snadno interpretovatelný.
"""
import pandas
import math
import matplotlib.pyplot as plt
platy = pandas.read_csv('platy_2021_02.csv')
max = math.ceil(platy['plat'].max()/10000)*10000
min = math.floor(platy['plat'].min()/10000)*10000
span = 2500
NumberOfBins = int((max-min)/span)

print(max, min, NumberOfBins)
bins=[]
for i in range(NumberOfBins):
  value = min + (i + 0.5) * span
  bins.append(value)

print(bins)
platy[['plat']].hist(bins=bins)
plt.show()


"""
Dobrovolný doplněk
Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist().
Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit.
Musíš vložit sloupec ve formě dat, nikoli pouze jeho název.

Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě,
ve kterém jednotliví pracovníci pracují (to jsme již dělali v příkladu) příkladu 26.
Následně sloupec mesto použij na rozdělení podgrafů.
"""
import pandas

import matplotlib.pyplot as plt

zam_plat = pandas.read_csv('zam_plat.csv')
zam_plat['plat'].hist(by=zam_plat['mesto'], bins=6)

plt.show()

