import os
import sys
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.race_manager import RaceManager
from src.nascar_data import NASCARData


class TestIntegrationPersistence(unittest.TestCase):
    def test_save_then_load_restores_state(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            state_file = tmp_path / "state.json"

            m1 = RaceManager()
            m1.add_race(NASCARData("Charlotte", 150))
            original_score = m1.total_score()

            m1.save_to_file(str(state_file))

            m2 = RaceManager()
            m2.load_from_file(str(state_file))

            self.assertEqual(m2.get_race_count(), 1)
            self.assertEqual(m2.total_score(), original_score)


if __name__ == "__main__":
    unittest.main()
