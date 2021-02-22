"""Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku.
 Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné.
 Napiš software, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit meeting room.
  Poté vypíše počet volných místností, které jsou k dispozici."""

volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = int(input('Na kolikátou hodinu chcete zamluvit meeting room? '))

if hodina not in volnePokoje:
  print('V tuto hodinu není volný žádný meeting room. Vybírejte mezi 9-12 hod.')
  hodina = int(input('Na kolikátou hodinu chcete zamluvit meeting room? '))
pocet = len(volnePokoje[hodina])
if hodina in volnePokoje and pocet == 1:
  print('V ' +str(hodina) + ' hodin je volný ' + str(pocet) + ' meeting room.')
elif hodina in volnePokoje and 2 <= pocet <= 4:
  print('V ' + str(hodina) + ' hodin jsou volné ' + str(pocet) + ' meeting roomy.')
else:
  print('V ' + str(hodina) + ' hodin je volných ' + str(pocet) + ' meeting roomů.')