import unittest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from services.manager import ReserveringManager, MAX_PERSONEN_PER_TIJDSLOT


class FakeStorage:
    """Test-storage die niets naar schijf schrijft, alleen in geheugen werkt."""

    def __init__(self):
        self.opgeslagen = []

    def load(self):
        return []

    def save(self, reserveringen):
        self.opgeslagen = list(reserveringen)


class TestReserveringManager(unittest.TestCase):

    def setUp(self):
        self.manager = ReserveringManager(FakeStorage())

    # Test 1: geldig toevoegen -> True + lijst groeit
    def test_voeg_toe_geldig(self):
        resultaat = self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 4)
        self.assertTrue(resultaat)
        self.assertEqual(len(self.manager.alles()), 1)

    # Test 2: lege naam -> False
    def test_voeg_toe_lege_naam(self):
        resultaat = self.manager.voeg_toe("", "2026-02-06", "18:30", 4)
        self.assertFalse(resultaat)
        self.assertEqual(len(self.manager.alles()), 0)

    # Test 3: aantal 0 -> False
    def test_voeg_toe_aantal_nul(self):
        resultaat = self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 0)
        self.assertFalse(resultaat)

    # Test 4: verwijderen geldige index -> True
    def test_verwijder_geldig(self):
        self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 4)
        resultaat = self.manager.verwijder(0)
        self.assertTrue(resultaat)
        self.assertEqual(len(self.manager.alles()), 0)

    # Test 5: verwijderen foute index -> False
    def test_verwijder_fout_index(self):
        resultaat = self.manager.verwijder(0)
        self.assertFalse(resultaat)

    # Test 6 (extra): max capaciteit per tijdslot
    def test_max_capaciteit_tijdslot(self):
        self.manager.voeg_toe("Jan", "2026-02-06", "18:30", MAX_PERSONEN_PER_TIJDSLOT - 5)
        resultaat = self.manager.voeg_toe("Piet", "2026-02-06", "18:30", 10)
        self.assertFalse(resultaat)

    # Test 7 (extra): zoeken op naam
    def test_zoek_op_naam(self):
        self.manager.voeg_toe("Jan Jansen", "2026-02-06", "18:30", 2)
        self.manager.voeg_toe("Piet Pietersen", "2026-02-06", "19:00", 2)
        resultaten = self.manager.zoek_op_naam("jan")
        self.assertEqual(len(resultaten), 1)
        self.assertEqual(resultaten[0].naam, "Jan Jansen")


if __name__ == "__main__":
    unittest.main()
