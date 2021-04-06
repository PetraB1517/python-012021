"""Projekty
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")
Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty
pro jednoho vybraného zákazníka.

Načti data ze souboru a ulož je do tabulky.
Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.

Dobrovolný doplněk
Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře,
tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka."""

import pandas
vykazy = pandas.read_csv('vykazy.csv')

print(vykazy)
print(vykazy.groupby('project')['hours'].sum())

# Doplněk

zam_plat = pandas.read_csv('zam_plat.csv')

vykazy = vykazy.rename(columns={'emloyee_id':'cislo_zamestnance'})

vykazy_zamestnancu = pandas.merge(zam_plat, vykazy, on=['cislo_zamestnance'])

print(vykazy_zamestnancu.groupby('mesto')['hours'].sum())
