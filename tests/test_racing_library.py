import sys
import os
import unittest
from datetime import date

# Allow imports from src/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.racing_library import (
    load_race_data,
    validate_driver_record,
    search_driver_results,
    filter_by_team,
    sort_races_by_date,
)


class TestRacingLibrary(unittest.TestCase):

    def test_validate_driver_record_valid(self):
        record = {"driver": "Lewis Hamilton", "team": "Mercedes"}
        self.assertTrue(validate_driver_record(record))

    def test_validate_driver_record_missing_field(self):
        record = {"driver": "Max Verstappen"}
        with self.assertRaises(ValueError):
            validate_driver_record(record)

    def test_search_driver_results(self):
        data = [
            {"driver": "Charles Leclerc", "team": "Ferrari"},
            {"driver": "Lando Norris", "team": "McLaren"},
        ]
        results = search_driver_results(data, "Lando")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["team"], "McLaren")

    def test_filter_by_team(self):
        data = [
            {"driver": "Lewis Hamilton", "team": "Mercedes"},
            {"driver": "George Russell", "team": "Mercedes"},
            {"driver": "Sergio Perez", "team": "Red Bull"},
        ]
        mercedes_drivers = filter_by_team(data, "Mercedes")
        self.assertEqual(len(mercedes_drivers), 2)

    def test_sort_races_by_date(self):
        data = [
            {"race": "Monaco GP", "date": "2025-05-25"},
            {"race": "Bahrain GP", "date": "2025-03-02"},
            {"race": "Italian GP", "date": "2025-09-07"},
        ]
        sorted_data = sort_races_by_date(data)
        self.assertEqual(sorted_data[0]["race"], "Bahrain GP")
        self.assertIsInstance(sorted_data[0]["date"], date)


if __name__ == "__main__":
    unittest.main()


