import json
from pathlib import Path

from models.reservering import Reservering


class ReserveringStorage:
    def __init__(self, filename="reserveringen.json"):
        self.filename = filename

    def load(self):
        pad = Path(self.filename)
        if not pad.exists():
            return []

        try:
            data = json.loads(pad.read_text(encoding="utf-8"))
            return [Reservering.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            return []

    def save(self, reserveringen):
        data = [r.to_dict() for r in reserveringen]
        Path(self.filename).write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
