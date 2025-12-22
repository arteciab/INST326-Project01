import json
import unittest
import tempfile
from pathlib import Path

from src.race_manager import RaceManager
from src.f1_data import F1Data
from src.nascar_data import NASCARData
from src.indycar_data import IndyCarData


class TestSaveLoadPersistence(unittest.TestCase):
    """
    Unit tests for RaceManager save/load persistence functionality.
    """

    def _make_manager_with_races(self):
        m = RaceManager()
        m.add_race(F1Data("Monaco GP", 78))
        m.add_race(NASCARData("Daytona 500", 200))
        m.add_race(IndyCarData("Indy 500", 200))
        return m

    def test_save_and_load_round_trip(self):
        m1 = self._make_manager_with_races()

        with tempfile.TemporaryDirectory() as tmp:
            save_file = Path(tmp) / "state.json"

            # Use the methods your system actually implements
            m1.save_to_file(str(save_file))

            m2 = RaceManager()
            m2.load_from_file(str(save_file))

            self.assertEqual(m2.get_race_count(), 3)

    def test_load_missing_file_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            m = RaceManager()
            with self.assertRaises(FileNotFoundError):
                m.load_from_file(str(missing))

    def test_load_corrupted_json_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"
            bad.write_text("{not valid json", encoding="utf-8")

            m = RaceManager()
            with self.assertRaises(Exception):
                m.load_from_file(str(bad))

    def test_load_unknown_race_type_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            save_file = Path(tmp) / "state.json"
            save_file.write_text(
                json.dumps({
                    "version": 1,
                    "races": [{"type": "WEC", "race_name": "Le Mans", "laps": 100}]
                }),
                encoding="utf-8",
            )

            m = RaceManager()
            with self.assertRaises(Exception):
                m.load_from_file(str(save_file))


if __name__ == "__main__":
    unittest.main(verbosity=2)
