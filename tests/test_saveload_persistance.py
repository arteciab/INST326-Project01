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
        manager = RaceManager()
        manager.add_race(F1Data("Monaco GP", 78))
        manager.add_race(NASCARData("Daytona 500", 200))
        manager.add_race(IndyCarData("Indy 500", 200))
        return manager

    def test_save_and_load_round_trip(self):
        """
        Saving and loading state should fully restore race objects.
        """
        manager = self._make_manager_with_races()

        with tempfile.TemporaryDirectory() as tmp:
            save_file = Path(tmp) / "state.json"

            manager.save_to_file(str(save_file))

            loaded = RaceManager()
            loaded.load_from_file(str(save_file))

            self.assertEqual(loaded.get_race_count(), 3)

    def test_load_missing_file_raises_file_not_found(self):
        """
        Loading a missing save file should raise FileNotFoundError.
        """
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            m = RaceManager()
            with self.assertRaises(FileNotFoundError):
                m.load_from_file(str(missing))


if __name__ == "__main__":
    unittest.main(verbosity=2)



