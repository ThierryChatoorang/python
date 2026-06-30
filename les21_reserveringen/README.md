# Reserveringssysteem Restaurant

Een CLI-applicatie waarmee een restaurant reserveringen kan bijhouden: toevoegen, bekijken, verwijderen, zoeken en filteren. Alle data wordt opgeslagen in een JSON-bestand zodat reserveringen bewaard blijven na het afsluiten van het programma.

## Wat doet de app?

- Reserveringen toevoegen (naam, datum, tijd, aantal personen)
- Alle reserveringen tonen
- Reserveringen verwijderen
- Zoeken op naam
- Filteren op datum
- Automatische controle op maximale capaciteit per tijdslot (max 30 personen)
- Validatie op alle invoer, zodat het programma nooit crasht door foute input

## Hoe start je hem?

Zorg dat je in de map `les21_reserveringen/` staat en run:

```
python main.py
```

Er verschijnt een menu in de terminal. Volg de instructies op het scherm.

## Features

| Feature | Beschrijving |
|---|---|
| Toevoegen | Maakt een nieuwe reservering aan, met validatie op naam, datum, tijd en aantal personen |
| Tonen | Print alle huidige reserveringen met nummer |
| Verwijderen | Verwijdert een reservering op basis van het getoonde nummer |
| Zoeken op naam | Toont alleen reserveringen waarvan de naam de zoekterm bevat |
| Filteren op datum | Toont alleen reserveringen op een specifieke datum |
| Max capaciteit | Een tijdslot (datum + tijd) mag in totaal niet meer dan 30 personen bevatten |
| Opslag | Alle wijzigingen worden direct opgeslagen in `reserveringen.json` |

## Projectstructuur

```
les21_reserveringen/
├── main.py                  # CLI-menu (input/output)
├── README.md
├── reserveringen.json       # wordt automatisch aangemaakt
├── models/
│   ├── __init__.py
│   └── reservering.py       # Reservering dataclass
├── services/
│   ├── __init__.py
│   ├── storage.py           # laden/opslaan naar JSON
│   └── manager.py           # logica + validatie
└── tests/
    ├── __init__.py
    └── test_reserveringen.py
```

De code is gesplitst per verantwoordelijkheid:
- **models** bevat alleen data (de `Reservering`-class).
- **services** bevat de logica (`ReserveringManager`) en de opslag (`ReserveringStorage`), los van elkaar.
- **main.py** bevat alleen het menu en de input/output, geen logica.

## Hoe run je de tests?

Vanuit de map `les21_reserveringen/`:

```
python -m unittest discover -s tests -v
```

Er zijn 7 tests die onder andere controleren:
- of geldig toevoegen werkt
- of een lege naam wordt geweigerd
- of een aantal van 0 wordt geweigerd
- of verwijderen werkt bij een geldige en een ongeldige index
- of de maximale capaciteit per tijdslot wordt afgedwongen
- of zoeken op naam correct filtert

De tests gebruiken een nep-opslagklasse (`FakeStorage`) zodat ze niets naar de echte `reserveringen.json` schrijven.

## Wat heb ik geleerd?

- Een project structureren in losse mappen (models, services, tests) in plaats van alles in één bestand
- Logica en opslag scheiden van elkaar, zodat ze los te testen zijn
- Validatie bouwen zodat foute invoer het programma niet laat crashen
- Een eigen businessregel (max capaciteit per tijdslot) toevoegen bovenop de basisfunctionaliteit
- Unittests schrijven met een "fake" opslag-object, zodat tests snel en herhaalbaar zijn zonder bestanden te overschrijven
- Stap voor stap bouwen: eerst alleen OOP-logica werkend krijgen, dan opslag toevoegen, dan pas de CLI eromheen bouwen
