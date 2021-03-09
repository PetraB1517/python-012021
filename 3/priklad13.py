"""Vrácení auta"""
"""
Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.

Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry,
a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal.
Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden,
a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta.
Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.

Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a jak dlouo ho měl půjčené.
Poté vypiš informaci o ceně.
"""


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

  def vrat_auto(self,tachograf,dny):
    self.kilometry += int(tachograf)
    self.stav = True
    cena1=400
    cena2=300
    dny = int(dny)

    if dny <= 7:
      cena = cena1*dny
    else:
      cena = cena2*dny

    return "Cena za půjčení auta je " + str(cena) + " Kč."


peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)

skoda = Auto("1P3 4747", "Škoda Octavia", 41253)


dotaz = input("Jakou značku auta jste si půjčili?")


vraceni = input("Kolik kilometrů jste najeli? ")
pocetDnu = input ("Kolik dnů jste měl auto půjčené?")

if dotaz == "Peugeot":
  print(peugeot.vrat_auto(vraceni,pocetDnu))
elif dotaz == "Škoda":
  print(skoda.vrat_auto(vraceni,pocetDnu))


print(peugeot.__dict__)
