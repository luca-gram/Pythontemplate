import random

# De functie laat de geraden letters in het woord zien en de niet geranden letters als _
def geef_geraden_letters_in_woord(woord, geraden_letters):
    gevonden_letters = ""
    for letter in woord:
        if letter in geraden_letters:
            gevonden_letters += letter
        else:
            gevonden_letters += "_"
    return gevonden_letters

# Deze functie laat zien hoeveel pogingen de gebruiker nog over heeft
def laat_pogingen_zien(pogingen):
    if pogingen == 1:
        print("Let op! Dit is je laatste poging!")
    else:
        print("Je hebt nog", pogingen, "pogingen over.")
           
WoordenGalgje = ["python", "informatica", "bartbrink", "laboratorium", "struisvogel", "scholier", "dinosaurus", "toetsweek", "docent", "middelbareschool", "computer", "programmeren", "fiets", "brachiosaurus", "schaar", "bikelife"]


opnieuw_spelen = True
while opnieuw_spelen == True:
      # De computer kiest een willekeurig woord uit de lijst
   Woord = random.choice(WoordenGalgje)
   pogingen = 5
   geraden_letters = set()
   print("Welkom bij galgje!")
   print("Je hebt 5 pogingen om het juiste woord te raden")
   print("Het woord heeft", len(Woord), "letters")

   gevonden = False

   while pogingen > 0 and gevonden == False:
      print("\nHuidige woord:", geef_geraden_letters_in_woord(Woord, geraden_letters))
      print("Geraden letters:", " ".join(sorted(geraden_letters)))
      letter = input("Kies een letter: ").lower()
      if len(letter) != 1 or not letter.isalpha():
         pogingen -= 1
         print("Je mag maar één letter invoeren! Probeer opnieuw.")
         laat_pogingen_zien(pogingen)
         continue
         
      # Controleren of de letter al geraden is
      if letter in geraden_letters:
         print("Je hebt deze letter al geraden. Probeer opnieuw.")
         geraden_letters.add(letter)
         laat_pogingen_zien(pogingen)
      # Controleren of de letter in het woord zit
      elif letter not in Woord:
        print("Fout! Deze letter is niet in het woord.")
        geraden_letters.add(letter)
        pogingen -= 1         
        laat_pogingen_zien(pogingen)
      elif letter in Woord:
        print("Goed geraden!")
        geraden_letters.add(letter)
        laat_pogingen_zien(pogingen)
   
      print()

     # Controleren of alle letters geraden zijn
      if all(letter in geraden_letters for letter in Woord):
        print("Gefeliciteerd! Je hebt het woord", Woord, "geraden!")
        geraden_letters.add(letter)
        gevonden = True

     # Controleren of er nog pogingen over zijn
      if pogingen == 0:
         print("Je hebt het woord niet geraden.")
         print("Het woord was:", Woord)
   # Hier wordt ge gebruiker gevraagd of hij nog een keer wil spelen
   antwoord = input("Wil je opnieuw spelen? (ja/nee): ").lower()
   if antwoord == "ja":
       opnieuw_spelen = True
   else:
       opnieuw_spelen = False
       print("Tot de volgende keer en bedankt voor het spelen!")