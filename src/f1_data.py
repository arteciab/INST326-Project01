
from abstract_race_data import AbstractRaceData

class F1Data(AbstractRaceData):
    """
    Race data for an F1 race.
    """

    def compute_performance_score(self):
        """
        Compute a simple performance score for an F1 race.

        F1 races may weigh laps differently.
        """
        return self._laps * 2.5