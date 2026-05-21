import random

GALG_FASEN = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

WOORDEN = [
    "appel",
    "banaan",
    "computer",
    "dinosaurus",
    "elektriciteit",
    "fiets",
    "gitaar",
    "herfst",
    "ijsberg",
    "jungle",
    "kameleon",
    "lantaarn",
    "magneet",
    "nachtvlinder",
    "olifant",
    "piraat",
    "quiche",
    "regenboog",
    "schildpad",
    "telefoon",
    "uiltje",
    "vliegtuig",
    "waterval",
    "xylofoon",
    "yoghurt",
    "zebra",
    "bibliotheek",
    "chocolade",
    "drempel",
    "energie",
    "festival",
    "gordijn",
    "horizon",
    "internet",
    "journalist",
    "koffie",
    "lampje",
    "muziek",
    "nachtmerrie",
    "oceaan",
    "puzzel",
    "radijs",
    "stormen",
    "trompet",
    "universiteit",
    "vogel",
    "wolkenkrabber",
    "kerstboom",
    "zandkasteel",
]


def toon_welkom():
    print("=" * 40)
    print("     WELKOM BIJ GALGJE!")
    print("=" * 40)
    print()


def toon_status(galg_fase, geraad, woord_letters, fout_letters):
    print(GALG_FASEN[galg_fase])
    print(f"Foute letters: {', '.join(sorted(fout_letters)) if fout_letters else '-'}")
    print()
    weergave = " ".join(letter if letter in geraad else "_" for letter in woord_letters)
    print(f"Woord: {weergave}")
    print(f"Pogingen over: {6 - galg_fase}")
    print()


def speel_ronde():
    woord = random.choice(WOORDEN)
    woord_letters = set(woord)
    geraad = set()
    fout_letters = set()
    pogingen = 12

    while True:
        toon_status(6 - pogingen, geraad, woord, fout_letters)

        if woord_letters <= geraad:
            print(f"🎉 Gefeliciteerd! Je hebt het woord geraden: '{woord.upper()}'")
            return True

        if pogingen == 0:
            print(f"💀 Game over! Het woord was: '{woord.upper()}'")
            return False
        print()
        letter = input("Raad een letter: ").lower().strip()
        print()

        if not letter:
            print("Typ een letter!")
            continue
        if len(letter) != 1:
            print("Typ slechts één letter.")
            continue
        if not letter.isalpha():
            print("Typ alleen een letter (a-z).")
            continue
        if letter in geraad or letter in fout_letters:
            print(f"Je hebt '{letter}' al geprobeerd!")
            continue

        if letter in woord_letters:
            geraad.add(letter)
            print(f"✅ Goed! '{letter}' zit in het woord.")
        else:
            fout_letters.add(letter)
            pogingen -= 1
            print(f"❌ Helaas, '{letter}' zit niet in het woord.")

        print()


def main():
    toon_welkom()

    while True:
        gewonnen = speel_ronde()

        print()
        opnieuw = input("Nog een keer spelen? (j/n): ").lower().strip()
        if opnieuw != "j":
            print()
            print("Bedankt voor het spelen! Tot de volgende keer. 👋")
            break
        print()


if __name__ == "__main__":
    main()
