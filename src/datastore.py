from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict
import csv
from pathlib import Path


@dataclass
class Driver:
    driver_id: str
    name: str
    team: str
    nationality: Optional[str] = None


@dataclass
class RaceResult:
    race_id: str
    date: datetime
    circuit: str
    season: int
    driver: Driver
    team: str
    position: Optional[int]
    points: float


class RaceDataStore:
    def __init__(self):
        self._results: List[RaceResult] = []

    @property
    def results(self):
        return list(self._results)

    def load_race_data(self, csv_path: str):
        path = Path(csv_path)
        if not path.exists():
            raise FileNotFoundError("File not found")

        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        loaded = 0
        for row in rows:
            # required basic fields in your CSV
            race_id = row.get("race_id", "").strip()
            date_str = row.get("date", "").strip()
            circuit = row.get("circuit", "").strip()
            driver_name = row.get("driver", "").strip()
            team = row.get("team", "").strip()

            if not race_id or not date_str or not circuit or not driver_name or not team:
                raise ValueError(f"Missing required data: {row}")

            try:
                if len(date_str) == 10:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                else:
                    date = datetime.fromisoformat(date_str)
            except Exception:
                raise ValueError(f"Bad date: {date_str}")

            season = date.year
            driver = self.validate_driver_data({
                "driver_id": driver_name,     # simple default
                "driver_name": driver_name,
                "team": team
            })

            position = None     # not in your CSV
            points = 0.0        # not in your CSV

            result = RaceResult(
                race_id=race_id,
                date=date,
                circuit=circuit,
                season=season,
                driver=driver,
                team=driver.team,
                position=position,
                points=points
            )
            self._results.append(result)
            loaded += 1

        self._results.sort(key=lambda x: x.date)
        return loaded

    def validate_driver_data(self, record: Dict):
        if "driver_id" not in record or "driver_name" not in record or "team" not in record:
            raise ValueError("Missing driver info")
        if str(record["driver_id"]).strip() == "" or str(record["driver_name"]).strip() == "" or str(record["team"]).strip() == "":
            raise ValueError("Driver fields cannot be empty")
        return Driver(
            driver_id=str(record["driver_id"]).strip(),
            name=str(record["driver_name"]).strip(),
            team=str(record["team"]).strip(),
            nationality=record.get("nationality")
        )

    def search_driver_results(self, name_or_id: str, season: Optional[int] = None):
        out = []
        key = name_or_id.strip().lower()
        for r in self._results:
            if season is not None and r.season != season:
                continue
            if r.driver.driver_id.lower() == key or r.driver.name.lower() == key:
                out.append(r)
        return sorted(out, key=lambda x: x.date)

    def filter_by_team(self, team: str, season: Optional[int] = None):
        out = []
        t = team.strip().lower()
        for r in self._results:
            if r.team.lower() == t and (season is None or r.season == season):
                out.append(r)
        return sorted(out, key=lambda x: x.date)

    def sort_races_by_date(self, ascending: bool = True):
        return sorted(self._results, key=lambda x: x.date, reverse=not ascending)
