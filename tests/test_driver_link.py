from src.datastore import RaceDataStore

def test_driver_profiles_exist_after_load():
    s = RaceDataStore()
    count = s.load_race_data("data/races_artecia.csv")  # falls back to races.csv if needed
    assert count > 0
    profiles = s.list_driver_profiles()
    assert len(profiles) >= 1
    # spot check a known name if present
    # assert s.get_driver("Dale Earnhardt") is not None
