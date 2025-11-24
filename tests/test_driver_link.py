import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.datastore import RaceDataStore

def test_driver_profiles_exist_after_load():
    s = RaceDataStore()
    count = s.load_race_data("data/races_artecia.csv")
    assert count > 0
    profiles = s.list_driver_profiles()
    assert len(profiles) >= 1
