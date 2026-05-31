def bereken_prijs(aantal, prijs_per_stuk):
    """berekent de totaalprijs voor een product"""
    return aantal * prijs_per_stuk


favoriete_snack = input("Wat is je favoriete snack?")
prijs_snack = input("Hoeveel kost " + favoriete_snack + " in euro's?")
favoriete_drankje = input("Wat is je favoriete drankje?")
prijs_drankje = input("Hoeveel kost " + favoriete_drankje + " in euro's?")

while True:
  try:
    aantal = int(input("Hoeveel combis wil je bestellen? "))
    if aantal >= 1:
        break
    print("Voer een getal van minimaal 1 in.")
  except ValueError:
    print("Dat is geen geldig getal, probeer opnieuw.")

Totaal_snacks = favoriete_snack * aantal
Totaal_drankjes = favoriete_drankje * aantal
subtotaal = Totaal_snacks +  Totaal_drankjes

if subtotaal > 20:  
    korting = subtotaal * 0.1

print("Je hebt " + str(aantal) + " combi's besteld.")
print("Je hebt " + str(Totaal_snacks) + " snacks besteld.")
print("Je hebt " + str(Totaal_drankjes) + " drankjes besteld.")
print("De subtotaal is " + str(subtotaal) + " euro.")
