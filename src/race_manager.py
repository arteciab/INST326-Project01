from __future__ import annotations
import json
from pathlib import Path

from src.f1_data import F1Data
from src.nascar_data import NASCARData
from src.indycar_data import IndyCarData


class RaceManager:
    """
    Manages a collection of race objects.

    This class demonstrates composition: it "has" race objects.
    """

    def __init__(self):
        """
        Initialize the manager with an empty list of races.
        """
        self._races = []
        self.selected_race_id = None

    def add_race(self, race_obj):
        """
        Add a race object to the manager.

        Args:
            race_obj: An object that has a compute_performance_score method.
        """
        self._races.append(race_obj)

    def total_score(self):
        """
        Add up the performance scores of all races.

        Returns:
            float: Sum of all race scores.
        """
        return sum(r.compute_performance_score() for r in self._races)

    def list_races(self):
        """
        Print basic info about all races in the manager.
        """
        for r in self._races:
            print(f"{type(r).__name__} - score: {r.compute_performance_score()}")

    def to_dict(self) -> dict:
        return {
            "version": 1,
            "selected_race_id": self.selected_race_id,
            "races": [race.to_dict() for race in self.races]
        }

    def save_state(self, path: str | Path) -> None:
        path = Path(path)
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent = 2)
        except OSError as e:
            raise RuntimeError(f"Could not save state to {path}: {e}") from e

    @classmethod
    def load_state(cls, path):
        path = Path(path)

        try:
            with path.open("r", encoding = "utf-8") as file:
                data = json.load(file)
        except FileNotFoundError as e:
            raise RuntimeError(f"State file not found: {path}")
        except json.JSONDecodeError:
            raise RuntimeError(f"State file is not valid JSON: {path}")
        except OSError as e:
            raise RuntimeError(f"Could not read state file: {path}: {e}")
        
        manager = cls()

        for race_data in data.get("races", []):
            race_type = race_data.get("type")

            if race_type == "F1":
                race = F1Data.from_dict(race_data)
            elif race_type == "NASCAR":
                race = NASCARData.from_dict(race_data)
            elif race_type == "IndyCar":
                race = IndyCarData.from_dict(race_data)
            else:
                raise ValueError(f"Unknown race type in saved state: {race_type}")
            manager.races.append(race)
        
        return manager
    

class RaceFactory:
    MAP = {
        "F1": F1Data,
        "NASCAR": NASCARData,
        "INDYCAR": IndyCarData,
    }

    @classmethod
    def from_dict(cls, data):
        return cls.MAP[data["type"]].from_dict(data)