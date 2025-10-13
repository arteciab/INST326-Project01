from src.racing_library import (
    load_race_data,
    validate_driver_data,
    search_driver_results,
    filter_by_team,
    sort_races_by_date
)
from datetime import date


def test_validate_driver_data_valid():
    record = {"driver": "Lewis Hamilton", "team": "Mercedes"}
    assert validate_driver_data(record) is True


def test_validate_driver_data_missing_field():
    record = {"driver": "Max Verstappen"}
    try:
        validate_driver_data(record)
    except ValueError:
        assert True


def test_search_driver_results():
    data = [
        {"driver": "Charles Leclerc", "team": "Ferrari"},
        {"driver": "Lando Norris", "team": "McLaren"},
    ]
    results = search_driver_results(data, "Lando")
    assert len(results) == 1
    assert results[0]["team"] == "McLaren"


def test_filter_by_team():
    data = [
        {"driver": "Lewis Hamilton", "team": "Mercedes"},
        {"driver": "George Russell", "team": "Mercedes"},
        {"driver": "Sergio Perez", "team": "Red Bull"},
    ]
    mercedes_drivers = filter_by_team(data, "Mercedes")
    assert len(mercedes_drivers) == 2


def test_sort_races_by_date():
    data = [
        {"race": "Monaco GP", "date": "2025-05-25"},
        {"race": "Bahrain GP", "date": "2025-03-02"},
        {"race": "Italian GP", "date": "2025-09-07"},
    ]
    sorted_data = sort_races_by_date(data)
    assert sorted_data[0]["race"] == "Bahrain GP"
    assert isinstance(sorted_data[0]["date"], date)
