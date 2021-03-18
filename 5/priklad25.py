"""Teplota ve městech podruhé
Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických
(sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US).
Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.

Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Phiadelphia.


Dobrovolný doplněk

Vrať se k pomocné tabulce, kterou jsi vytvořila v bodu 2. Vypiš průměrnou hodnotu ze všech měření,
která byla provedena 13. listopadu 2017 na úzení Spojených států amerických.
K tomu využij funkci .mean(), která funguje stejně jako funkce .sum(), kterou jsme si ukazovali na lekci.
Pokud znáš základy statistiky, zkus funkci pro medián .median() a rozptyl .var().
"""
import pandas
teploty = pandas.read_csv('temperature.csv')

import pytemperature
teploty["AvgTempCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

print(teploty.head())


# Dotaz na řádky z 13. listopadu 2017

print(teploty[teploty['Day'] == 13])


# Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických
tempUS13 = teploty[(teploty['Day'] == 13) & (teploty['Country'] == 'US')]
print(tempUS13.head())


# Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Phiadelphia.

print(tempUS13[tempUS13['City'].isin(['Washington', 'Phiadelphia'])])


# Dobrovolný úkol

avgTempUS = tempUS13['AvgTempCelsia'].mean()
print('Průměrná teplota v  USA 13. listopadu 2017 byla ' + str(round(avgTempUS*10)/10) + ' °C.')

medianTempUS = tempUS13['AvgTempCelsia'].median()
varTempUS = tempUS13['AvgTempCelsia'].var()
odchylkaTempUS = (varTempUS)**(1/2)

print('Medián je ' + str(round(medianTempUS*10)/10) + ' °C, rozptyl ' + str(round(varTempUS*100)/100) +
      ' (°C)^2 a směrodatná odchylka je ' + str(round(odchylkaTempUS*10)/10) + ' °C.')
