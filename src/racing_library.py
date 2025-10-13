from datetime import datetime, date
import csv, json, os


def load_race_data(source):
    if isinstance(source, str):
        if not os.path.exists(source):
            raise FileNotFoundError(f"File not found: {source}")
        ext = os.path.splitext(source)[1].lower()
        if ext == ".csv":
            with open(source, newline="", encoding="utf-8") as f:
                data = list(csv.DictReader(f))
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
                record["date"] = datetime.strptime(str(record["date"]), "%Y-%m-%d").date()
            except Exception:
                raise ValueError(f"Invalid date format: {record['date']}")
    return data


def validate_driver_data(record):
    if not isinstance(record, dict):
        raise TypeError("Record must be a dictionary.")
    for key in ("driver", "team"):
        if key not in record or not record[key]:
            raise ValueError(f"Missing required field: {key}")
    return True


def search_driver_results(data, driver_name):
    if not isinstance(driver_name, str):
        raise TypeError("Driver name must be a string.")
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")
    name = driver_name.lower()
    return [r for r in data if name in str(r.get("driver", "")).lower()]


def filter_by_team(data, team_name):
    if not isinstance(team_name, str):
        raise TypeError("Team name must be a string.")
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")
    return [r for r in data if str(r.get("team", "")).lower() == team_name.lower()]


def sort_races_by_date(data, descending=False):
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")

    out = []
    for rec in data:
        r = dict(rec)
        d = r.get("date")
        if isinstance(d, date):
            parsed = d
        else:
            try:
                parsed = datetime.strptime(str(d), "%Y-%m-%d").date()
            except Exception:
                raise ValueError(f"Invalid date format in record: {d}")
        r["date"] = parsed
        out.append(r)

    return sorted(out, key=lambda x: x["date"], reverse=bool(descending))
