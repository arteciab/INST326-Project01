from __future__ import annotations
from pathlib import Path
from typing import Iterable


def load_finish_times(path: str | Path) -> list[float]:
    """
    Read one numeric finish time per line from a text file.

    Returns:
        list[float]: Parsed times.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If no valid numeric lines are found.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    times: list[float] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            times.append(float(line.strip()))
        except ValueError:
            continue
    if not times:
        raise ValueError(f"No valid finish times found in {p}.")
    return times


def calculate_average_finish_from_file(path: str | Path) -> float:
    """
    Convenience wrapper: load finish times from file and return the mean.

    Example:
        >>> import tempfile
        >>> tmp = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        >>> _ = tmp.write("10\\n20\\n")
        >>> tmp.flush()
        >>> round(calculate_average_finish_from_file(tmp.name), 2)
        15.0
    """
    times = load_finish_times(path)
    return sum(times) / len(times)


def calculate_average_finish(times: Iterable[float]) -> float:
    """
    Calculate the average finish time from an iterable of floats.

    Args:
        times: Iterable of numeric times (e.g., [83.1, 84.0, 82.7]).

    Returns:
        float: Mean time.

    Raises:
        ValueError: If there are no times after validation.
        TypeError: If any element cannot be converted to float.
    """
    cleaned: list[float] = []
    for t in times:
        try:
            cleaned.append(float(t))
        except Exception as exc:
            raise TypeError(f"Non-numeric time: {t!r}") from exc
    if not cleaned:
        raise ValueError("No times provided.")
    return sum(cleaned) / len(cleaned)


def validate_driver_rows(rows: list[dict]) -> list[tuple[str, float]]:
    """
    Validate driver rows that contain 'Driver Name' and 'Finish Time'.

    Args:
        rows: list of dictionaries (e.g., from CSV DictReader).

    Returns:
        list of (name, time) tuples for valid rows.

    Notes:
        - Skips invalid rows silently (library stays pure).
        - Use reporting to show user-friendly messages if needed.
    """
    valid: list[tuple[str, float]] = []
    for row in rows:
        name = str(row.get("Driver Name", "")).strip()
        time_str = str(row.get("Finish Time", "")).strip()
        if not name:
            continue
        try:
            time = float(time_str)
            if time < 0:
                continue
        except ValueError:
            continue
        valid.append((name, time))
    return valid


def search_driver_results(rows: list[dict], driver_name: str) -> list[dict]:
    """
    Return rows for a specific driver (case-insensitive exact match).

    Args:
        rows: list of dictionaries with 'Driver Name' and 'Finish Time'.
        driver_name: driver to match.

    Returns:
        list[dict]: Matching rows.
    """
    needle = driver_name.lower()
    out: list[dict] = []
    for row in rows:
        name = str(row.get("Driver Name", "")).strip()
        if name.lower() == needle:
            out.append(row)
    return out


def filter_by_team(rows: list[dict], team_name: str) -> list[dict]:
    """
    Filter rows by team (case-insensitive exact match).

    Args:
        rows: list of dictionaries with 'Team' and related fields.
        team_name: team to match.

    Returns:
        list[dict]: Matching rows.
    """
    needle = team_name.lower()
    out: list[dict] = []
    for row in rows:
        team = str(row.get("Team", "")).strip()
        if team.lower() == needle:
            out.append({
                "Driver Name": str(row.get("Driver Name", "")).strip(),
                "Team": team,
                "Finish Time": str(row.get("Finish Time", "")).strip(),
                **{k: v for k, v in row.items() if k not in {"Driver Name", "Team", "Finish Time"}},
            })
    return out


def sort_rows_by_race_date(rows: list[dict], descending: bool = False) -> list[dict]:
    """
    Sort rows by 'Race Date' (expects 'YYYY-MM-DD').

    Args:
        rows: list of dictionaries that include 'Race Date' as a string.
        descending: sort newest first when True.

    Returns:
        list[dict]: New list with the same dicts, sorted by date.

    Raises:
        ValueError: If a row has an invalid 'Race Date' format.
    """
    from datetime import datetime

    def parse_date(s: str) -> datetime:
        try:
            return datetime.strptime(s, "%Y-%m-%d")
        except Exception as exc:
            raise ValueError(f"Invalid 'Race Date': {s!r} (expected YYYY-MM-DD)") from exc

    enriched = []
    for row in rows:
        date_str = str(row.get("Race Date", "")).strip()
        if not date_str:
            raise ValueError("Missing 'Race Date' in row.")
        dt = parse_date(date_str)
        enriched.append((dt, row))
    enriched.sort(key=lambda t: t[0], reverse=bool(descending))
    return [row for _, row in enriched]
