from abc import ABC, abstractmethod

class AbstractRaceData(ABC):
    """
    Abstract base class for race data across all motorsport types.
    Every specific type of race will inherit from this class.
    """

    def __init__(self, race_name, laps):
        """
        Initialize race attributes shared by all race types.

        Args:
            race_name (str): The name of the race.
            laps (int): The number of laps in the race.
        """
        self._race_name = race_name
        self._laps = laps

    @abstractmethod
    def compute_performance_score(self):
        """
        Calculate a performance score for this race.

        This method must be overridden by each subclass.
        """
        pass

    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__.replace("Data", "").upper(),
            "race_name": self._race_name,
            "laps": self._laps,
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        obj = cls.__new__(cls)
        obj._laps = data["laps"]
        return obj