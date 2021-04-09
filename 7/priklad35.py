"""Teplota ve městech popáté
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech."""

import pandas
import matplotlib.pyplot as plt

teploty = pandas.read_csv('temperature.csv')
teploty = teploty[teploty['City'].isin(['Helsinki', 'Miami Beach', 'Tokyo'])]
print(teploty)
teploty.boxplot(column='AvgTemperature', by='City')
plt.show()




