from datetime import datetime, date
import csv
import json
import os


def load_race_data(source):
    """
    Load race data from a CSV, JSON, or list of dictionaries.
    Returns a list of race records with parsed dates.
    """
    if isinstance(source, str):
        if not os.path.exists(source):
            raise FileNotFoundError(f"File not found: {source}")
        ext = os.path.splitext(source)[1].lower()
        if ext == ".csv":
            with open(source, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = list(reader)
        elif ext == ".json":
            with open(source, encoding="utf-8") as f:
                data = json.load(f)
        else:
            raise ValueError("Only .csv or .json files are supported.")
    elif isinstance(source, list):
        data = source
    else:
        raise TypeError("Source must be a filepath or list of dictionaries.")

    for record in data:
        if "date" in record:
            try:
                record["date"] = datetime.strptime(record["date"], "%Y-%m-%d").date()
            except Exception:
                raise ValueError(f"Invalid date format: {record['date']}")

    return data


def validate_driver_data(record):
    """
    Validate that a driver record contains required information.
    Returns True if valid, otherwise raises an error.
    """
    if not isinstance(record, dict):
        raise TypeError("Record must be a dictionary.")

    required = ["driver", "team"]
    for key in required:
        if key not in record or not record[key]:
            raise ValueError(f"Missing required field: {key}")

    return True


def search_driver_results(data, driver_name):
    """
    Search race results for a specific driver (case-insensitive).
    Returns a list of results.
    """
    if not isinstance(driver_name, str):
        raise TypeError("Driver name must be a string.")
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")

    driver_name = driver_name.lower()
    return [r for r in data if driver_name in str(r.get("driver", "")).lower()]


def filter_by_team(data, team_name):
    """
    Filter race results to include only those from a specific team.
    Returns a list of filtered records.
    """
    if not isinstance(team_name, str):
        raise TypeError("Team name must be a string.")
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")

    return [r for r in data if str(r.get("team", "")).lower() == team_name.lower()]


def sort_races_by_date(data, descending=False):
    """
    Sort race records by date.
    Returns a new list sorted by race date.
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")

    def get_date(record):
        d = record.get("date")
        if isinstance(d, date):
            return d
        try:
            return datetime.strptime(str(d), "%Y-%m-%d").date()
        except Exception:
            raise ValueError(f"Invalid date format in record: {d}")

    return sorted(data, key=get_date, reverse=descending)