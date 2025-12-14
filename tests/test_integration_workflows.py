import os
import sys
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.race_manager import RaceManager
from src.nascar_data import NASCARData
from src.f1_data import F1Data
from src.indycar_data import IndyCarData


class TestIntegrationWorkflows(unittest.TestCase):
    def test_to_dict_contains_expected_keys(self):
        m = RaceManager()
        m.add_race(NASCARData("Charlotte", 150))
        snap = m.to_dict()

        self.assertIn("version", snap)
        self.assertIn("races", snap)
        self.assertEqual(len(snap["races"]), 1)
        self.assertEqual(snap["races"][0]["type"], "NASCARData")
        self.assertEqual(snap["races"][0]["race_name"], "Charlotte")
        self.assertEqual(snap["races"][0]["laps"], 150)

    def test_from_dict_rebuilds_correct_subclass_types(self):
        data = {
            "version": 1,
            "races": [
                {"type": "NASCARData", "race_name": "Charlotte", "laps": 150},
                {"type": "F1Data", "race_name": "Spa", "laps": 44},
                {"type": "IndyCarData", "race_name": "Indy 500", "laps": 200},
            ],
        }

        m = RaceManager()
        m.from_dict(data)

        snap = m.to_dict()
        types = [r["type"] for r in snap["races"]]
        self.assertEqual(types, ["NASCARData", "F1Data", "IndyCarData"])

    def test_total_score_matches_expected_math(self):
        m = RaceManager()
        m.add_race(NASCARData("Charlotte", 150))  # 150 * 1.2 = 180
        m.add_race(F1Data("Spa", 44))             # 44 * 2.5 = 110
        m.add_race(IndyCarData("Indy 500", 200))  # 200 * 1.8 = 360

        self.assertEqual(m.total_score(), 180 + 110 + 360)

    def test_save_creates_file(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            state_file = tmp_path / "state.json"

            m = RaceManager()
            m.add_race(NASCARData("Charlotte", 150))
            m.save_to_file(str(state_file))

            self.assertTrue(state_file.exists())
            self.assertGreater(state_file.stat().st_size, 0)

    def test_load_missing_file_raises(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = tmp_path / "does_not_exist.json"

            m = RaceManager()
            with self.assertRaises(FileNotFoundError):
                m.load_from_file(str(missing))


if __name__ == "__main__":
    unittest.main()
