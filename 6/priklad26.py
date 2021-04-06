"""Zaměstnanci
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci.
Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.
Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021.
Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to,
že v naší firmě již nepracuje.
Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
"""

import pandas
zam_liberec = pandas.read_csv('zam_liberec.csv')
zam_plzen = pandas.read_csv('zam_plzeň.csv')
zam_praha = pandas.read_csv('zam_praha.csv')

#Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
zam_liberec['mesto'] = 'Liberec'
zam_plzen['mesto'] = 'Plzeň'
zam_praha['mesto'] = 'Praha'

#Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)

#Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021.
platy_unor = pandas.read_csv('platy_2021_02.csv')

#Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.

zam_plat = pandas.merge(zamestnanci, platy_unor, on=['cislo_zamestnance'])
#zam_plat.to_csv('zam_plat.csv', index=False)

#Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to,
#že v naší firmě již nepracuje.
print(zamestnanci.shape)
print(platy_unor.shape)
print(zam_plat.shape)

zam_plat_outer = pandas.merge(zamestnanci, platy_unor, on=['cislo_zamestnance'], how="outer")
print(zam_plat_outer[zam_plat_outer['plat'].isnull()])

#Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
print(zamestnanci.columns)

print(zam_plat.groupby('mesto')['plat'].mean())

#Doplněk

"""
Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují.
Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV
"""

pocet_byvalych_zamestnancu = zam_plat_outer.shape[0] - zam_plat.shape[0]
pocet_byvalych_zamestnancu2 = zam_plat_outer[zam_plat_outer['plat'].isnull()].shape[0]

byvaly_zamestnanci = zam_plat_outer[zam_plat_outer['plat'].isnull()]
del byvaly_zamestnanci['plat']

byvaly_zamestnanci.to_csv('byvaly_zamestnanci.csv', index=False)