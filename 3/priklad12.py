"""Půjčení auta
Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.

Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
Funkce zkontroluje, jestli je vozidlo aktuálně volné.
Pokud je volné, změní hodnotu atributu, který určuje, zda je vozidlo půjčené,
a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla)
jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
Uživatel může zadávat hodnoty Peugeot nebo Škoda.
Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto.

Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát."""


class Auto:
  def __init__(self, spz, znackaATyp,kilometry):
    self.spz = spz
    self.znackaATyp = znackaATyp
    self.kilometry = kilometry
    self.stav = True

  def pujc_auto(self):
    if self.stav:
      self.stav = False
      print("Potvrzuji zapůjčení vozidla.")
    else:
      print("Vozidlo není k dispozici.")

  def get_info(self):
    return "SPZ auta: "+ self.spz +", značka a typ: "+ self.znackaATyp

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)

skoda = Auto("1P3 4747", "Škoda Octavia", 41253)


dotaz = input("Jakou značku auta si přejete?")

if dotaz == "Peugeot":
  print(peugeot.get_info())
  peugeot.pujc_auto()
elif dotaz == "Škoda":
  print(skoda.get_info())
  skoda.pujc_auto()
else:
  print("Tato značka v naší půjčovně není k dispozici.")

dotaz = input("Jakou značku auta si přejete?")

if dotaz == "Peugeot":
  print(peugeot.get_info())
  peugeot.pujc_auto()
elif dotaz == "Škoda":
  print(skoda.get_info())
  skoda.pujc_auto()
else:
  print("Tato značka v naší půjčovně není k dispozici.")



