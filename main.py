def vraagcijfer():
    cijfer = float(input("Geef een cijfer "))
    return cijfer

cijfer1 = vraagcijfer()
cijfer2 = vraagcijfer()
gemiddelde = (cijfer1 +cijfer2) / 2
print("Je gemiddelde is  " + str(gemiddelde))