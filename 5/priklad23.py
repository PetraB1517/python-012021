"""Vakcíny
Stáhni si soubor country_vaccinations.csv o průběhu očkování proti nemoci COVID-19.
Stažení souboru pomocí wget:
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

Dále napiš následující dotazy:
Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10
(s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modeul datetime, ale vlož do dotazu přímo řetězec).
Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.
Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí
nebo naopak méně než 100 lidí.

Dobrovolný doplněk

Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy.
Použij např. funkci isin().
Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09.
Data v tomto formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce, tj. opět nemusíš použít modul datetime.
"""
import pandas
vakcinace = pandas.read_csv('country_vaccinations.csv')

# Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10

ockovaniDoDne = vakcinace[vakcinace['date'] == '2021-03-10']
print(ockovaniDoDne[['country', 'total_vaccinations']])


# Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.

ockovanoPresMil = vakcinace[(vakcinace['date'] == '2021-03-10') & (vakcinace['total_vaccinations'] > 1_000_000)]
print(ockovanoPresMil[['country', 'total_vaccinations']])


# Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí
# nebo naopak méně než 100 lidí.

extremy = vakcinace[(vakcinace['date'] == '2021-03-10') & ((vakcinace['daily_vaccinations'] < 100) | (vakcinace['daily_vaccinations'] > 100_000))]

print(extremy[['country', 'daily_vaccinations']])


# Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy.

print(vakcinace[(vakcinace['date'].isin(['2021-03-10', '2021-03-11'])) & (vakcinace['country'].isin(['United Kingdom', 'Finland', 'Italy']))])


# Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09.

print(vakcinace[(vakcinace['country'] == 'Japan') & (vakcinace['date'] >= '2021-03-03') & (vakcinace['date'] <= '2021-03-09')])
