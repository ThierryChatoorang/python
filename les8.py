from abc import ABC, abstractmethod


class Betaalmethode(ABC):

    def __init__(self, naam):
        self.naam = naam

    @abstractmethod
    def betaal(self, bedrag):
        pass


class PinBetaling(Betaalmethode):

    def __init__(self):
        super().__init__("Pin")

    def betaal(self, bedrag):
        print(f"Betaling gepind: €{bedrag}")


class ContantBetaling(Betaalmethode):

    def __init__(self):
        super().__init__("Contant")

    def betaal(self, bedrag):
        print(f"Contant ontvangen: €{bedrag}")


class OnlineBetaling(Betaalmethode):

    def __init__(self):
        super().__init__("Online")

    def betaal(self, bedrag):
        print(f"Online verwerkt: €{bedrag}")


methodes = [PinBetaling(), ContantBetaling(), OnlineBetaling()]

for methode in methodes:
    methode.betaal(49.95)