from src.abstract_race_data import AbstractRaceData

class NASCARData(AbstractRaceData):
    """
    Represents race data for a NASCAR event.
    Inherits shared attributes and behaviors from AbstractRaceData.
    """

    def compute_performance_score(self):
        """
        Compute a simple performance score for a NASCAR race.
        
        Returns:
            float: Score based on laps multiplied by a NASCAR-specific factor.
        """
        return self._laps * 1.2
