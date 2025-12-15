from abc import ABC, abstractmethod


class AbstractRaceData(ABC):
    def __init__(self, race_name, laps):
        self._race_name = race_name
        self._laps = laps

    @abstractmethod
    def compute_performance_score(self):
        pass
