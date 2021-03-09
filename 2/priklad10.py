"""Klíč k úspěchu"""
"""
Obchodníci v naší softwarové firmě používají jednoduchý systém, aby odhadli šanci na úspěch potenciální zakázky.
Každé zakázce přiřadí body od 0 do 10 a platí:

Pokud má zakázka méně než 5 bodů, šance na získání je malá.
Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
Pokud má zakázka více bodů, šance na získání je vysoká.


Body přidělují podle následujících kritérií:

Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.

Obrat: Firma nejlépe prodává zákazníkům se středním obratem. U malých většinou neuspěje, u velkých občas ano.
Pokud má firma obrat menší než 10 mil. Euro, přičti 0. Pokud je mezi 10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.

Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně v Německu a ve Francii (1 bod). 
Ostatním zemím dej 0.

Konference: Firma loni pořádala odbornou konferenci pro zákazníky.
Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.

Newsletter: Firma též rozesílá newsletter o svém produktu. Pokud zákazník newsletter odebírá, přičti 1 bod.

Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False. Funkce vrátí šanci na získání zakázky jako řetězec."""


def uspech_zakazky(odvetvi,obrat,zeme,konference=False,newsletter=False):
  body=0
  obrat=str(obrat)

  if odvetvi == 'automotive':
    body += 3
  elif odvetvi == 'retail':
    body += 2

  if "mil" in obrat:
    obrat = obrat.replace("mil","")
    obrat = obrat.replace(" ","")
  else:
    obrat = obrat.replace(" ","")
    obrat = obrat.replace("000000","")

  if 10 <= int(obrat) <= 1000:
    body += 3
  elif int(obrat) > 1000:
    body += 1

  if zeme == "Česko" or "Slovensko":
    body += 2
  elif zeme == "Německo" or "Francie":
    body += 1

  if konference:
    body += 1

  if newsletter:
    body +=1


  if body > 8:
    print("Šance na získání zakázky je vysoká.")
  elif body <= 5:
    print("Šance na získání zakázky je malá.")
  else:
    print("Šance na získání zakázky je střední.")







