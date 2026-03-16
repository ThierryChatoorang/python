class Product:

    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(f"{self.naam} - €{self.prijs} (voorraad: {self._voorraad})")

    def is_op_voorraad(self):
        return self._voorraad > 0

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            print("Aantal moet groter zijn dan 0.")
            return False
        if self._voorraad < aantal:
            print(f"Niet genoeg voorraad voor {self.naam}.")
            return False
        self._voorraad -= aantal
        return True


class Winkelmandje:

    def __init__(self):
        self.items = []

    def voeg_toe(self, product, aantal):
        if aantal <= 0:
            print("Aantal moet groter zijn dan 0.")
            return
        if product._voorraad < aantal:
            print(f"Niet genoeg voorraad voor {product.naam}.")
            return
        self.items.append((product, aantal))
        print(f"Toegevoegd: {product.naam} x{aantal}")

    def toon_mandje(self):
        if not self.items:
            print("Mandje is leeg.")
            return
        for product, aantal in self.items:
            print(f"{product.naam} x{aantal} - €{product.prijs * aantal}")
        print(f"Totaal: €{self.totaal_prijs()}")

    def totaal_prijs(self):
        return sum(product.prijs * aantal for product, aantal in self.items)


producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5),
]

mandje = Winkelmandje()

while True:
    print("\n1 - Producten bekijken")
    print("2 - Product toevoegen")
    print("3 - Mandje bekijken")
    print("4 - Afrekenen")
    print("0 - Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        for i, product in enumerate(producten):
            print(f"{i + 1}. ", end="")
            product.toon_info()

    elif keuze == "2":
        for i, product in enumerate(producten):
            print(f"{i + 1}. ", end="")
            product.toon_info()
        nummer = input("Kies productnummer: ")
        if not nummer.isdigit() or not (1 <= int(nummer) <= len(producten)):
            print("Ongeldig productnummer.")
        else:
            gekozen = producten[int(nummer) - 1]
            aantal_input = input("Hoeveel wil je? ")
            if not aantal_input.isdigit() or int(aantal_input) <= 0:
                print("Ongeldig aantal.")
            else:
                mandje.voeg_toe(gekozen, int(aantal_input))

    elif keuze == "3":
        mandje.toon_mandje()

    elif keuze == "4":
        if not mandje.items:
            print("Mandje is leeg.")
        else:
            totaal = mandje.totaal_prijs()
            if totaal > 500:
                korting = totaal * 0.10
                totaal = totaal - korting
                print(f"10% korting toegepast! Korting: €{korting:.2f}")
            succes = True
            for product, aantal in mandje.items:
                if not product.verlaag_voorraad(aantal):
                    succes = False
                    break
            if succes:
                print(f"Bedankt voor je aankoop! Totaal: €{totaal:.2f}")
                mandje.items = []

    elif keuze == "0":
        print("Tot ziens!")
        break

    else:
        print("Ongeldige keuze.")