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
           
WoordenGalgje = ["python", "informatica", "bart brink", "laboratorium", "struisvogel", "scholier", "dinosaurus", "toetsweek", "docent", "middelbareschool", "computer", "programmeren", "fiets", "brachiosaurus"]
Woord = random.choice(WoordenGalgje)

print(Woord)

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

   # Controleren of de letter al geraden is
   if letter in geraden_letters:
      print("Je hebt deze letter al geraden. Probeer opnieuw.")
      geraden_letters.add(letter)
      print("Je hebt nog", pogingen, "pogingen over.")
   # Controleren of de letter in het woord zit
   elif letter not in Woord:
      print("Fout! Deze letter is niet in het woord.")
      geraden_letters.add(letter)
      pogingen -= 1         
      print("Je hebt nog", pogingen, "pogingen over.")
   elif letter in Woord:
      print("Goed geraden!")
      geraden_letters.add(letter)
      print("Je hebt nog", pogingen, "pogingen over.")
   
   print()

   # Controleren of alle letters geraden zijn
   if all(letter in geraden_letters for letter in Woord):
      print("Gefeliciteerd! Je hebt het woord geraden!")
      gevonden = True

   # Controleren of er nog pogingen over zijn
   if pogingen == 0:
       print("Je hebt het woord niet geraden.")
       print("Het woord was:", Woord)
