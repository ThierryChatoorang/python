from models.reservering import Reservering

MAX_PERSONEN_PER_TIJDSLOT = 30


class ReserveringManager:
    def __init__(self, storage):
        self.storage = storage
        self.reserveringen = storage.load()

    def _bezetting_tijdslot(self, datum, tijd):
        return sum(
            r.aantal_personen
            for r in self.reserveringen
            if r.datum == datum and r.tijd == tijd
        )

    def voeg_toe(self, naam, datum, tijd, aantal):
        if not naam or not naam.strip():
            return False
        if not datum or not datum.strip():
            return False
        if not tijd or not tijd.strip():
            return False
        if not isinstance(aantal, int) or aantal <= 0:
            return False

        # Extra 3: max capaciteit per tijdslot
        huidige_bezetting = self._bezetting_tijdslot(datum, tijd)
        if huidige_bezetting + aantal > MAX_PERSONEN_PER_TIJDSLOT:
            return False

        reservering = Reservering(naam.strip(), datum.strip(), tijd.strip(), aantal)
        self.reserveringen.append(reservering)
        self.storage.save(self.reserveringen)
        return True

    def alles(self):
        return self.reserveringen

    def verwijder(self, index):
        if index < 0 or index >= len(self.reserveringen):
            return False

        self.reserveringen.pop(index)
        self.storage.save(self.reserveringen)
        return True

    def zoek_op_naam(self, zoekterm):
        zoekterm = zoekterm.lower()
        return [r for r in self.reserveringen if zoekterm in r.naam.lower()]

    def filter_op_datum(self, datum):
        return [r for r in self.reserveringen if r.datum == datum]
