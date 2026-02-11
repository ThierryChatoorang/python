# Stap 1: Class maken
class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    # Stap 5: Methode toevoegen
    def is_volwassen(self):
        return self.leeftijd >= 18


# Stap 2: Drie objecten maken
s1 = Student("Ali", 19)
s2 = Student("Sara", 20)
s3 = Student("Jan", 17)

# Stap 3: In een lijst zetten
studenten = [s1, s2, s3]

# Stap 6: Teller maken
aantal_volwassen = 0

# Stap 4 + 5 + 6: For-loop gebruiken
for student in studenten:
    print("Naam:", student.naam)
    print("Leeftijd:", student.leeftijd)
    print("Volwassen:", student.is_volwassen())
    print("------------------")

    if student.is_volwassen():
        aantal_volwassen += 1

# Totaal printen
print("Aantal studenten van 18 jaar of ouder:", aantal_volwassen)
