import random

WoordenGalgje = ["Python", "informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering"]
Woord = random.choice(WoordenGalgje)

pogingen = 5
geraden_letters = set()
print("Welkom bij galgje!")
print("Je hebt 5 pogingen om het juiste woord te raden")
print("Het woord heeft", len(Woord), "letters")

while pogingen > 0:
   print("\nHuidige woord:", " ".join([letter if letter in geraden_letters else "_" for letter in Woord]))
   print("Geraden letters:", " ".join(sorted(geraden_letters)))
   input("kies een letter: ")
   break

letter = input("Kies een letter: ").lower()

  if letter in geraden_letters:
   print("Je hebt deze letter al geraden. Probeer opnieuw.")
continue
   geraden_letters.add(letter)
   if letter in Woord:
      print("Goed geraden!")
      if all(letter in geraden_letters for letter in Woord):
         print("Gefeliciteerd! Je hebt het woord geraden:", Woord)
         else:
         print("Fout! De letter is niet in het woord.")
         pogingen -= 1
         print("Je hebt nog", pogingen, "pogingen over.")
     






