from src.persistence import save_state, load_state
from src.nascar_data import NASCARData
from src.f1_data import F1Data
from src.indycar_data import IndyCarData

import json
from pathlib import Path


_RACE_TYPE_MAP = {
    "NASCARData": NASCARData,
    "F1Data": F1Data,
    "IndyCarData": IndyCarData,
    # a couple aliases in case older saves/tests use them
    "NASCAR": NASCARData,
    "F1": F1Data,
    "IndyCar": IndyCarData,
}


class RaceManager:
    def __init__(self):
        self._races = []

    def add_race(self, race_obj):
        self._races.append(race_obj)

    def get_race_count(self):
        return len(self._races)

    def to_dict(self):
        return {
            "version": 1,
            "races": [
                {
                    "type": type(r).__name__,
                    "race_name": r._race_name,
                    "laps": r._laps,
                }
                for r in self._races
            ],
        }

    def from_dict(self, data):
        self._races = []

        races = data.get("races")
        if races is None or not isinstance(races, list):
            raise ValueError("State file missing races list")

        for item in races:
            race_type = item.get("type")
            race_name = item.get("race_name")
            laps = item.get("laps")

            if race_type is None or race_name is None or laps is None:
                raise ValueError("Race entry missing required fields")

            cls = _RACE_TYPE_MAP.get(race_type)
            if cls is None:
                raise ValueError(f"Unknown race type: {race_type}")

            self._races.append(cls(race_name, laps))

        return self

    def save_to_file(self, file_path: str):
        save_state(self.to_dict(), file_path)

    def load_from_file(self, file_path: str):
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(str(path))

        data = load_state(str(path))
        self.from_dict(data)
        return self

    @classmethod
    def load_state(cls, file_path):
        # tests want RuntimeError for corrupted JSON specifically
        try:
            path = Path(file_path)
            raw = path.read_text(encoding="utf-8")
            data = json.loads(raw)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
            raise RuntimeError("Could not load saved state") from e

        mgr = cls()
        mgr.from_dict(data)
        return mgr

    def total_score(self):
        total = 0
        for r in self._races:
            total += r.compute_performance_score()
        return total

    def list_races(self):
        for r in self._races:
            print(f"{type(r).__name__} - score: {r.compute_performance_score()}")
