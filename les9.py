def vraag_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")


def delen(a, b):
    if b == 0:
        raise ZeroDivisionError("Delen door 0 mag niet.")
    return a / b


while True:
    print("\n1 - Optellen")
    print("2 - Delen")
    print("0 - Stoppen")

    keuze = vraag_int("Kies: ")

    if keuze == 0:
        print("Tot ziens!")
        break

    elif keuze == 1:
        a = vraag_int("Eerste getal: ")
        b = vraag_int("Tweede getal: ")
        print(f"Uitkomst: {a + b}")

    elif keuze == 2:
        try:
            a = vraag_int("Eerste getal: ")
            b = vraag_int("Tweede getal: ")
            print(f"Uitkomst: {delen(a, b)}")
        except ZeroDivisionError as e:
            print(f"Fout: {e}")
        finally:
            print("Terug naar menu...")

    else:
        print("Ongeldige keuze.")