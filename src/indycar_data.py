from abstract_race_data import AbstractRaceData

class IndyCarData(AbstractRaceData):
    """
    Race data for an IndyCar race.
    """

    def compute_performance_score(self):
        """
        Compute a simple performance score for an IndyCar race.
        """
        return self._laps * 1.8