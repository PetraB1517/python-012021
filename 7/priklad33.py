#Twilio podruhé
"""Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020. Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.

Stažení souboru pomocí wget:

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím.
Porovnej grafy a zjisti, co se změnilo.
"""

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")


# Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.

plt.figure(1,figsize=(10,5))
plt.plot(twilio['Date'], twilio['Close'])

plt.xticks(range(0,twilio['Date'].count(), 50))
plt.xlabel('Datum')
plt.ylabel('Hodnota')
plt.title('Vývoj ceny')
#plt.show()

#Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím.
#Porovnej grafy a zjisti, co se změnilo.

twilio["Date"] = pandas.to_datetime(twilio["Date"])
plt.figure(2,figsize=(10,5))
plt.plot(twilio['Date'], twilio['Close'])
plt.xlabel('Datum')
plt.ylabel('Hodnota')
plt.title('Vývoj ceny')
plt.show()
#automaticky naformátuje přehledněji časovou osu

"""Dobrovolný doplněk
Přidej ke grafům popisky os a titulky. Po zavolání funkce plot() si výsledek ulož do proměnné ax.
Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.

ax = twilio.plot()
ax.set_ylabel("Cena v dolarech")
Obdobně využij metody set_title() a set_xlabel() a nastav popisek osy x a titulek grafu."""

#udělala jsem to sama a jinak :D