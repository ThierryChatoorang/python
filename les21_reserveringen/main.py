from services.storage import ReserveringStorage
from services.manager import ReserveringManager


def vraag_int(tekst):
    invoer = input(tekst).strip()
    if not invoer.isdigit():
        return None
    return int(invoer)


def toon_reserveringen(manager, reserveringen=None):
    lijst = reserveringen if reserveringen is not None else manager.alles()

    if not lijst:
        print("(Geen reserveringen)")
        return

    print("\n--- Reserveringen ---")
    for i, r in enumerate(manager.alles() if reserveringen is None else reserveringen, start=1):
        print(f"{i}. {r.naam} | {r.datum} {r.tijd} | {r.aantal_personen} personen")
    print()


def menu():
    storage = ReserveringStorage()
    manager = ReserveringManager(storage)

    while True:
        print("=== RESERVERINGSSYSTEEM RESTAURANT ===")
        print("1) Toon reserveringen")
        print("2) Voeg reservering toe")
        print("3) Verwijder reservering")
        print("4) Zoek op naam")
        print("5) Filter op datum")
        print("0) Stoppen")

        keuze = input("Kies: ").strip()

        if keuze == "1":
            toon_reserveringen(manager)

        elif keuze == "2":
            naam = input("Naam: ").strip()
            datum = input("Datum (bv. 2026-02-06): ").strip()
            tijd = input("Tijd (bv. 18:30): ").strip()
            aantal = vraag_int("Aantal personen: ")

            if aantal is None:
                print("Aantal personen moet een geldig getal zijn.")
                continue

            gelukt = manager.voeg_toe(naam, datum, tijd, aantal)
            if gelukt:
                print("Reservering toegevoegd!")
            else:
                print("Reservering kon niet worden toegevoegd (controleer invoer of capaciteit).")

        elif keuze == "3":
            toon_reserveringen(manager)
            if manager.alles():
                nummer = vraag_int("Welke reservering verwijderen (nummer): ")
                if nummer is None or not (1 <= nummer <= len(manager.alles())):
                    print("Ongeldig nummer.")
                else:
                    manager.verwijder(nummer - 1)
                    print("Reservering verwijderd!")

        elif keuze == "4":
            zoekterm = input("Zoek op naam: ").strip()
            resultaten = manager.zoek_op_naam(zoekterm)
            toon_reserveringen(manager, resultaten)

        elif keuze == "5":
            datum = input("Filter op datum (bv. 2026-02-06): ").strip()
            resultaten = manager.filter_op_datum(datum)
            toon_reserveringen(manager, resultaten)

        elif keuze == "0":
            print("Tot ziens!")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    menu()
