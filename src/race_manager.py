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
