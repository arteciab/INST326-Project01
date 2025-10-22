# src/racing_library.py
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import List, Dict

import csv
import json
import os


def load_race_data(source: str | List[Dict]) -> List[Dict]:
    """
    Load race records from a .csv/.json file path or from an in-memory list of dicts.
    If a 'date' field is present, parse it as YYYY-MM-DD into a datetime.date.

    Args:
        source: Path to a .csv or .json file, or a list of dict records.

    Returns:
        list[dict]: Records with 'date' normalized to datetime.date when present.

    Raises:
        FileNotFoundError: If the given file path does not exist.
        ValueError: If the extension is not .csv/.json or a date is invalid.
        TypeError: If source is neither a str nor a list of dictionaries.

    Examples:
        >>> rows = load_race_data([{"driver": "A", "team": "X", "date": "2024-05-01"}])
        >>> isinstance(rows[0]["date"], date)
        True
    """
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
        raise TypeError("Source must be a filepath (str) or list[dict].")

    for record in data:
        if "date" in record and record["date"] not in (None, ""):
            try:
                record["date"] = datetime.strptime(str(record["date"]), "%Y-%m-%d").date()
            except Exception as exc:
                raise ValueError(f"Invalid date format: {record['date']}") from exc
    return data


def load_csv_rows(path: str | Path) -> List[Dict]:
    """
    Load a CSV file into a list of dictionaries (no additional normalization).

    Args:
        path: CSV file path.

    Returns:
        list[dict]: Rows as dictionaries.

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> import tempfile
        >>> p = Path(tempfile.gettempdir()) / "demo.csv"
        >>> _ = p.write_text("Driver Name,Team\\nA,Ferrari\\n", encoding="utf-8")
        >>> rows = load_csv_rows(p)
        >>> rows[0]["Driver Name"], rows[0]["Team"]
        ('A', 'Ferrari')
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate_driver_record(record: Dict) -> bool:
    """
    Validate that a single record has non-empty 'driver' and 'team' fields.

    Args:
        record: A single race/entry record.

    Returns:
        True if valid.

    Raises:
        TypeError: If record is not a dict.
        ValueError: If 'driver' or 'team' is missing/empty.

    Examples:
        >>> validate_driver_record({"driver": "Lewis Hamilton", "team": "Mercedes"})
        True
    """
    if not isinstance(record, dict):
        raise TypeError("Record must be a dictionary.")
    for key in ("driver", "team"):
        val = record.get(key)
        if val is None or str(val).strip() == "":
            raise ValueError(f"Missing required field: {key}")
    return True


def search_driver_results(data: List[Dict], driver_name: str) -> List[Dict]:
    """
    Case-insensitive substring match for 'driver' within the dataset.

    Args:
        data: List of records (dicts) containing a 'driver' field.
        driver_name: The name or partial name to search for.

    Returns:
        list[dict]: Matching records.

    Raises:
        TypeError: If argument types are wrong.

    Examples:
        >>> search_driver_results([{"driver": "Max Verstappen"}], "max")
        [{'driver': 'Max Verstappen'}]
    """
    if not isinstance(driver_name, str):
        raise TypeError("Driver name must be a string.")
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")
    needle = driver_name.lower()
    return [r for r in data if needle in str(r.get("driver", "")).lower()]


def filter_by_team(data: List[Dict], team_name: str) -> List[Dict]:
    """
    Exact, case-insensitive match for 'team'.

    Args:
        data: List of records with a 'team' field.
        team_name: Team name to match.

    Returns:
        list[dict]: Records whose team matches.

    Raises:
        TypeError: If argument types are wrong.

    Examples:
        >>> filter_by_team([{"team": "Ferrari"}, {"team": "McLaren"}], "ferrari")
        [{'team': 'Ferrari'}]
    """
    if not isinstance(team_name, str):
        raise TypeError("Team name must be a string.")
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")
    return [r for r in data if str(r.get("team", "")).lower() == team_name.lower()]


def sort_races_by_date(data: List[Dict], descending: bool = False) -> List[Dict]:
    """
    Sort records by the 'date' field. Accepts either datetime.date or 'YYYY-MM-DD'.

    Args:
        data: List of records containing a 'date' field.
        descending: If True, newest first.

    Returns:
        list[dict]: New list sorted by date (original list is not mutated).

    Raises:
        TypeError: If data is not a list.
        ValueError: If any record has an invalid date value.

    Examples:
        >>> sorted_rows = sort_races_by_date([{"date": "2024-01-02"}, {"date": "2024-01-01"}])
        >>> str(sorted_rows[0]["date"])
        '2024-01-01'
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list of race records.")

    out: List[Dict] = []
    for rec in data:
        r = dict(rec)
        d = r.get("date")
        if isinstance(d, date):
            parsed = d
        else:
            try:
                parsed = datetime.strptime(str(d), "%Y-%m-%d").date()
            except Exception as exc:
                raise ValueError(f"Invalid date format in record: {d}") from exc
        r["date"] = parsed
        out.append(r)

    return sorted(out, key=lambda x: x["date"], reverse=bool(descending))
