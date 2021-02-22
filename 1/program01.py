"""Níže máš slovník, který obsahuje kódy balíků s informací, zda již byl balík předán kurýrovi k doručení.
  Pokud byl předán, má hodnotu True, v opačném případě má hodnotu False.
  Napiš program pro operátora společnosti, který poskytuje informaci, zda byl balík předán kurýrovi.
  Nejprve se uživatele zeptej na kód balíku. Následně podle hodnoty ve slovníku vypiš větu Balík byl předán kurýrovi nebo
  Balík zatím nebyl předán kurýrovi."""
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

dotaz = input('Vložte kód balíku: ')

if dotaz not in baliky:
  print('Balík s tímto kódem nebyl nalezen.')
else:
  if baliky[dotaz]:
    print("Balík " + dotaz + " byl předán kurýrovi")
  else:
    print("Balík " + dotaz + " zatím nebyl předán kurýrovi")
