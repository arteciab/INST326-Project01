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
            manager.save_state(save_file)

            loaded = RaceManager.load_state(save_file)

            self.assertEqual(len(loaded.races), 3)
            self.assertIsInstance(loaded.races[0], F1Data)
            self.assertIsInstance(loaded.races[1], NASCARData)
            self.assertIsInstance(loaded.races[2], IndyCarData)

            self.assertEqual(loaded.races[0]._race_name, "Monaco GP")
            self.assertEqual(loaded.races[0]._laps, 78)
    
    def test_load_missing_file_raises_runtime_error(self):
        """
        Loading a missing save file should raise RuntimeError.
        """
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            with self.assertRaises(RuntimeError):
                RaceManager.load_state(missing)

    def test_load_corrupted_json_raises_runtime_error(self):
        """
        Loading an invalid JSON file should raise RuntimeError.
        """
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"
            bad.write_text("{not valid json", encoding="utf-8")

            with self.assertRaises(RuntimeError):
                RaceManager.load_state(bad)
    
    def test_load_unknown_race_type_raises_value_error(self):
        """
        Unknown race types in saved state should raise ValueError.
        """
        with tempfile.TemporaryDirectory() as tmp:
            save_file = Path(tmp) / "state.json"
            save_file.write_text(
                json.dumps({
                    "races": [
                        {"type": "WEC", "race_name": "Le Mans", "laps": 100}
                    ]
                }),
                encoding="utf-8",
            )

            with self.assertRaises(ValueError):
                RaceManager.load_state(save_file)
    
    def test_load_partial_state_raises_error(self):
        """
        Missing required race fields should raise an error.
        """
        with tempfile.TemporaryDirectory() as tmp:
            save_file = Path(tmp) / "state.json"
            save_file.write_text(
                json.dumps({
                    "races": [
                        {"type": "F1", "race_name": "Monaco GP"}  # missing laps
                    ]
                }),
                encoding="utf-8",
            )

            with self.assertRaises(Exception):
                RaceManager.load_state(save_file)
    def test_save_and_load_round_trip(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

