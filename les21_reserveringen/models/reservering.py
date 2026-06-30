from dataclasses import dataclass, asdict


@dataclass
class Reservering:
    naam: str
    datum: str          # bv. "2026-02-06"
    tijd: str            # bv. "18:30"
    aantal_personen: int

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Reservering(
            naam=data["naam"],
            datum=data["datum"],
            tijd=data["tijd"],
            aantal_personen=data["aantal_personen"],
        )
