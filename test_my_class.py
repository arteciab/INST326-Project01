from pathlib import Path
from src.datastore import RaceDataStore

def pick_data_path():
    p1 = Path("data/races_artecia.csv")
    p2 = Path("data/races.csv")
    return str(p1) if p1.exists() else str(p2)

store = RaceDataStore()
path = pick_data_path()
count = store.load_race_data(path)
print("Loaded rows from:", path, "count:", count)

print("\nNewest first:")
for r in store.sort_races_by_date(ascending=False):
    print(r.race_id, r.driver.name, r.team, r.points)

drivers = sorted({r.driver.name for r in store.results})
teams = sorted({r.team for r in store.results})
print("\nDrivers in data:", drivers)
print("Teams in data:", teams)

if drivers:
    who = drivers[0]
    print(f"\nSearch by driver: {who}")
    for r in store.search_driver_results(who):
        print(r.race_id, r.driver.name, r.team)

if teams:
    t = teams[0]
    print(f"\nFilter by team: {t}")
    for r in store.filter_by_team(t):
        print(r.race_id, r.driver.name, r.team)
