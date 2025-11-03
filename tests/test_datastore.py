from pathlib import Path
from src.datastore import RaceDataStore

def _pick():
    a = Path("data/races_artecia.csv")
    b = Path("data/races.csv")
    return str(a) if a.exists() else str(b)

def test_load_and_sort():
    store = RaceDataStore()
    n = store.load_race_data(_pick())
    assert n > 0
    s = store.sort_races_by_date()
    assert len(s) == n
    assert s[0].date <= s[-1].date

def test_search_and_filter_do_not_crash():
    store = RaceDataStore()
    store.load_race_data(_pick())
    _ = store.search_driver_results("Rajah Caruth")
    _ = store.filter_by_team("Hendrick Motorsports")
