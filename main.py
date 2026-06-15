import random

def geef_geraden_letters_in_woord(woord, geraden_letters):
    gevonden_letters = ""
    for letter in woord:
        if letter in geraden_letters:
            gevonden_letters += letter
        else:
            gevonden_letters += "_"
    return gevonden_letters

WoordenGalgje = ["python", "informatica", "bartbrink", "laboratorium", "struisvogel", "scholier", "dinosaurus", "toetsweek", "docent", "middelbareschool", "computer", "programmeren", "fiets", "brachiosaurus"]

def speel_spel():
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

        if letter in geraden_letters:
            print("Je hebt deze letter al geraden. Probeer opnieuw.")
            print("Je hebt nog", pogingen, "pogingen over.")
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

        if all(l in geraden_letters for l in Woord):
            print("Gefeliciteerd! Je hebt het woord geraden!")
            gevonden = True

        if pogingen == 0:
            print("Je hebt het woord niet geraden.")
            print("Het woord was:", Woord)

while True:
    speel_spel()
    antwoord = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    if antwoord != "ja":
        print("Tot de volgende keer!")
        break
