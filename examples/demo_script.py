from src.racing_library import (
    load_race_data,
    validate_driver_record,   # <- was validate_driver_data
    search_driver_results,
    filter_by_team,
    sort_races_by_date,
)


def main():
    races = [
        {"race_id": "1", "date": "2024-02-01", "circuit": "Bahrain", "driver": "Alice", "team": "Alpha"},
        {"race_id": "2", "date": "2024-01-20", "circuit": "Monaco",  "driver": "Bob",   "team": "Beta"},
        {"race_id": "3", "date": "2024-03-10", "circuit": "Melbourne","driver": "Alice","team": "Alpha"},
    ]

    data = load_race_data(races)
    validate_driver_record({"driver": "Alice", "team": "Alpha"})

    print("Search for Alice:", [r["race_id"] for r in search_driver_results(data, "Alice")])
    print("Filter by team Alpha:", [r["race_id"] for r in filter_by_team(data, "Alpha")])
    print("Sorted by date:", [r["race_id"] for r in sort_races_by_date(data)])


if __name__ == "__main__":
    main()
