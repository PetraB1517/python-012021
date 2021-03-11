# Streamovací služba

"""Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani.
Třídám Serial a Film přidej funkce get_celkova_delka().
Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr.
Vytvoř objekt, který reprezentuje nějakého uživatele.

Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty.


Složitější varianta
V pokročilejší variantě neeviduj pouze délku sledování ale i to,
jaké pořady uživatel sledoval. Dále přidej funkci zhledni_polozku()
a funkci delka_sledování() pro uživatele,
která projde položky v seznamu a vrátí celkovou délku všech pořadů, které uživatel zhlédl.

Vytvoř si ukázkové objekty a ověř, že vše funguje."""

class Polozka:
  def __init__(self,jmeno,zanr):
    self.jmeno = jmeno
    self.zanr = zanr

  def get_info(self):
    print(self.jmeno + ", " + self.zanr)

  def vyber_polozku(self):
    return self.jmeno



class Film(Polozka):
  def __init__(self, jmeno,zanr,delka):
    super().__init__(jmeno,zanr)
    self.delka = delka

  def get_info(self):
    super().get_info()
    return "Délka filmu: " + str(self.delka) + " min\n"

  def get_celkova_delka(self):
    return self.delka




class Serial(Polozka):
  def __init__(self,jmeno,zanr, pocetEpizod, delkaEpizody):
    super().__init__(jmeno,zanr)
    self.pocetEpizod = pocetEpizod
    self.delkaEpizody = delkaEpizody

  def get_info(self):
    super().get_info()
    return "Seriál, počet epizod: " + str(self.pocetEpizod) + ", délka jedné epizody: " + str(self.delkaEpizody) + " min\n"

  def get_celkova_delka(self):
    return self.delkaEpizody * self.pocetEpizod




class Uzivatel:
  def __init__(self, uzivatelske_jmeno):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = 0
    self.zhlednuto = []

  def pripocti_zhlednuti(self, delka):
    self.delka_sledovani += delka

  def zhledni_polozku(self, polozka):
    self.zhlednuto.append(polozka)

  def seznam_zhlednuto(self):
    print("Seznam zhlédnutých pořadů: \n")
    for item in self.zhlednuto:
      print(item.get_info())

  def delka_sledovanych(self):
    delka_sledovani = 0
    for item in self.zhlednuto:
      delka_sledovani += item.get_celkova_delka()
    delka_hod = delka_sledovani//60
    delka_min = delka_sledovani%60
    print("Celková délka zhlédnutých pořadů je: " +str(delka_hod) + " hod a " + str(delka_min) + " min")


film = Film("Copak je to za vojáka", "komedie", 86)
film2 = Film("Vykoupení z věznice Shawshank", "drama", 233)
serial = Serial("DARK", "sci-fi", 10, 53)

pepa21 = Uzivatel("pepa21")


pepa21.zhledni_polozku(serial)
pepa21.pripocti_zhlednuti(serial.get_celkova_delka())

pepa21.zhledni_polozku(film)
pepa21.zhledni_polozku(film2)

pepa21.seznam_zhlednuto()


pepa21.delka_sledovanych()


# print(pepa21.__dict__)
