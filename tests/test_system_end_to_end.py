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


class TestSystemEndToEnd(unittest.TestCase):

    def test_full_save_load_workflow(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            state_file = tmp_path / "state.json"

            m1 = RaceManager()
            m1.add_race(NASCARData("Charlotte", 150))
            m1.add_race(F1Data("Spa", 44))
            original_score = m1.total_score()

            m1.save_to_file(str(state_file))

            m2 = RaceManager()
            m2.load_from_file(str(state_file))

            self.assertEqual(m2.get_race_count(), 2)
            self.assertEqual(m2.total_score(), original_score)

    def test_import_simulation_then_export_state(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            state_file = tmp_path / "state.json"

            m = RaceManager()
            m.add_race(NASCARData("Charlotte", 150))
            m.add_race(IndyCarData("Indy 500", 200))

            m.save_to_file(str(state_file))

            self.assertTrue(state_file.exists())
            self.assertGreater(state_file.stat().st_size, 0)

    def test_restart_and_continue_analysis(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            state_file = tmp_path / "state.json"

            m1 = RaceManager()
            m1.add_race(NASCARData("Charlotte", 150))
            m1.save_to_file(str(state_file))

            m2 = RaceManager()
            m2.load_from_file(str(state_file))

            m2.add_race(F1Data("Spa", 44))

            self.assertEqual(m2.get_race_count(), 2)
            self.assertEqual(
                m2.total_score(),
                (150 * 1.2) + (44 * 2.5)
            )


if __name__ == "__main__":
    unittest.main()

