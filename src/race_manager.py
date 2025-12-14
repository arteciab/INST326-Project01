from src.persistence import save_state, load_state
from src.nascar_data import NASCARData
from src.f1_data import F1Data
from src.indycar_data import IndyCarData

_RACE_TYPE_MAP = {
    "NASCARData": NASCARData,
    "F1Data": F1Data,
    "IndyCarData": IndyCarData,
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
        for item in data.get("races", []):
            cls = _RACE_TYPE_MAP[item["type"]]
            race_obj = cls(item["race_name"], item["laps"])
            self._races.append(race_obj)

    def save_to_file(self, file_path: str):
        save_state(self.to_dict(), file_path)

    def load_from_file(self, file_path: str):
        data = load_state(file_path)
        self.from_dict(data)

    def total_score(self):
        return sum(r.compute_performance_score() for r in self._races)

    def list_races(self):
        for r in self._races:
            print(f"{type(r).__name__} - score: {r.compute_performance_score()}")
