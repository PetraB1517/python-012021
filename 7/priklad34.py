#Velikonoce
"""Ze souboru velikonoce.csv načti data o tom, kolikrát na který datum připadaly Velikonoce v letech 1600 až 2100.

import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")
Vytvoř sloupcový graf, který data přehledně zobrazí.
Na ose x budou vidět jednotlivá data ("datumy") a výška sloupce označí, kolikrát na daný den připadly Velikonoce.
Tentokrát jsou popisky a titulek povinné :-)

Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(),
abys nastavila popisek osy y grafu.

ax = velikonoce.plot()
ax.set_ylabel("Počet dnů")"""


import pandas
import matplotlib.pyplot as plt

velikonoce = pandas.read_csv('velikonoce.csv')
velikonoce = velikonoce.set_index('Datum')

plt.figure(1)
ax = velikonoce.plot(kind='bar')
ax.set_xlabel("Datum")
ax.set_ylabel("Počet dnů")
ax.set_title('Velikonoční dny')
ax.tick_params(axis='x', labelrotation=65, labelsize='small')
ax.get_legend().remove()
#plt.show()




"""Rozšířené zadání

Vytvoř si datový soubor sama. Můžeš k tomu využít modul dateutil, který při instalaci najdeš pod jménem python-dateutil.
Následně si zkopíruj kód níže a doplň na místo komentářů příkazy, které prováději požadovanou činnost."""

import pandas
from dateutil import easter

data = []
for rok in range(1900,2020):
  datum = easter.easter(rok)
  datum = datum.strftime('%d.%m.')
  data.append(datum)


data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()

plt.figure(1)
ax = data.plot(kind='bar')
ax.set_xlabel("Datum")
ax.set_ylabel("Počet dnů")
ax.set_title('Velikonoční dny')
ax.tick_params(axis='x', labelrotation=65, labelsize='small')
plt.show()