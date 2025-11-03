from __future__ import annotations
from pathlib import Path
from typing import Iterable
from collections import defaultdict
from datetime import datetime
import csv


class MotorsportAnalytics:
    """
    A class for managing and analyzing motorsport race data.

    This class provides methods to compare drivers, summarize team
    performance, list top drivers, and analyze trends over time.
    """

    def __init__(self, data_source: str | Path):
        # Validate data source
        path = Path(data_source)
        if not path.exists():
            raise FileNotFoundError(f"Data file not found: {path}")

        self._data_source = path       # private attribute for file path
        self._rows: list[dict] = self._load_csv(path)  # private attribute for race data

        if not self._rows:
            raise ValueError("No race data found in the file.")

    # Properties for Encapsulation

    @property
    def data_source(self) -> Path:
        # Return the path of the data file
        return self._data_source

    @property
    def rows(self) -> list[dict]:
        # Return a safe copy of the race data
        return list(self._rows)

    # Private Helper Methods
    def _load_csv(self, path: Path) -> list[dict]:
        # Load race data from a CSV file
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(f))

    @staticmethod
    def _calculate_average_finish(times: Iterable[float]) -> float:
        # Compute the average finish time from a list of numeric values
        values = [float(t) for t in times if str(t).strip()]
        if not values:
            raise ValueError("No valid finish times provided.")
        return sum(values) / len(values)

    # Core Instance Methods


    def compare_drivers(self, driver1: str, driver2: str) -> dict:
        # Compare two drivers' average finish times and determine the better one
        d1_rows = [r for r in self._rows if r["Driver Name"].lower() == driver1.lower()]
        d2_rows = [r for r in self._rows if r["Driver Name"].lower() == driver2.lower()]

        d1_times = [float(r["Finish Time"]) for r in d1_rows if r.get("Finish Time")]
        d2_times = [float(r["Finish Time"]) for r in d2_rows if r.get("Finish Time")]

        d1_avg = self._calculate_average_finish(d1_times) if d1_times else None
        d2_avg = self._calculate_average_finish(d2_times) if d2_times else None

        winner = None
        if d1_avg and d2_avg:
            winner = driver1 if d1_avg < d2_avg else driver2

        return {
            driver1: {"average_finish": d1_avg, "races": len(d1_rows)},
            driver2: {"average_finish": d2_avg, "races": len(d2_rows)},
            "winner": winner,
        }

    def team_performance_summary(self) -> list[dict]:
        # Calculate each team's average finish time and number of entries
        team_data = defaultdict(list)
        for r in self._rows:
            team = str(r.get("Team", "")).strip()
            try:
                team_data[team].append(float(r["Finish Time"]))
            except Exception:
                continue

        summary = []
        for team, times in team_data.items():
            avg = self._calculate_average_finish(times)
            summary.append({
                "Team": team,
                "Average Finish": round(avg, 2),
                "Entries": len(times),
            })

        return sorted(summary, key=lambda x: x["Average Finish"])

    def get_top_drivers(self, top_n: int = 5) -> list[tuple[str, float]]:
        # Return the top N drivers ranked by best (lowest) average finish time
        driver_times = defaultdict(list)
        for r in self._rows:
            name = str(r.get("Driver Name", "")).strip()
            try:
                driver_times[name].append(float(r["Finish Time"]))
            except Exception:
                continue

        averages = [
            (driver, self._calculate_average_finish(times))
            for driver, times in driver_times.items() if times
        ]
        return sorted(averages, key=lambda x: x[1])[:top_n]

    def analyze_performance_trends(self, driver_name: str) -> list[tuple[str, float]]:
        # Return a list of (date, finish_time) pairs for one driver, sorted by date
        results = [
            (r["Race Date"], float(r["Finish Time"]))
            for r in self._rows
            if r["Driver Name"].lower() == driver_name.lower()
        ]
        results.sort(key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
        return results

    # String Representations
    def __str__(self) -> str:
        # User-friendly string summary
        return f"MotorsportAnalytics with {len(self._rows)} race records"

    def __repr__(self) -> str:
        # Developer-friendly class representation
        return f"<MotorsportAnalytics source={self._data_source!r} records={len(self._rows)}>"
