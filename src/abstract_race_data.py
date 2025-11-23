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
