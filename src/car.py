from typing import Iterable, List, Tuple, Optional

class Car:
    def __init__(
        self,
        model_year: int,
        team: str,
        engine_maker: str,
        driver: Driver,
        results: Optional[Iterable[Result]] = None,
    ):
        if not isinstance(model_year, int):
            raise TypeError("Model Year must be an int")
        if not isinstance(team, str):
            raise TypeError("Team must be a string")
        if not isinstance(engine_maker, str):
            raise TypeError("Engine Manufacturer must be a string")
        if not isinstance(driver, Driver):
            raise TypeError("Driver must be a Driver object")
        if results is not None and not all(isinstance(r, Result) for r in results):
            raise TypeError("results must be an iterable of Result objects")

        self.__model_year = model_year
        self.__team = team
        self.__engine_maker = engine_maker
        self.__driver = driver
        self.__results: List[Result] = list(results) if results else []

    def get_car_details(self):
        """
        Return A summary of this Car's core metadata.

        Returns: dict[str, object]: a mapping with keys
            - "Team: str
            - "Driver": Driver
            - "Engine maker": str
            - "Model year": int
        Raise: None.

        Example:
        >>> car = Car(2025, "Ferrari", "Ferrari", "Charles Leclerc")
        >>> details = car.get_car_details()
        >>> details["Team"]
        'Ferrari'
        >>> details["Model year"]
        2025
        """    
        return {
            "Team": self.__team,
            "Driver": self.__driver,
            "Engine maker": self.__engine_maker,
            "Model year": self.__model_year
        }

    @property
    def results(self):
        """
    Read-only view of this car's race results.

    Returns:
        tuple[Result, ...]: The results currently recorded for this car,
        in insertion order.

    Raises:
        None.

    Example:
        >>> car = Car(2025, "Ferrari", "Ferrari", "Charles Leclerc")
        >>> car.results
        ()
        >>> _ = car.add_result(Result("Monaco GP", 1, 73.254, 25.0))
        >>> len(car.results)
        1
        """
        return tuple(self.__results)
    
    def add_result(self, result: Result):
        """
    Append a single race result to this car.

    Args:
        result (Result): The result to add.

    Returns:
        None.

    Raises:
        TypeError: If `result` is not an instance of `Result`.

    Example:
        >>> car = Car(2025, "Ferrari", "Ferrari", "Charles Leclerc")
        >>> car.add_result(Result("Monaco GP", 1, 73.254, 25.0))
        >>> car.results[0].position
        1
    """
        if not isinstance(result, Result):
            raise TypeError("result must be a Result")
        self.__results.append(result)

    def best_lap(self) -> Optional[Result]:
        """
    Return the result with the lowest lap time for this car.

    Returns:
        Result | None: The `Result` instance with the minimum `lap_time`,
        or `None` if the car has no results.

    Raises:
        None.

    Example:
        >>> car = Car(2025, "Ferrari", "Ferrari", "Charles Leclerc")
        >>> car.add_result(Result("Monaco GP", 1, 73.254, 25.0))
        >>> car.add_result(Result("Italian GP", 3, 71.982, 15.0))
        >>> best = car.best_lap()
        >>> round(best.lap_time, 3)
        71.982
    """
        if not self.__results:
            return None
        return min(self.__results, key=lambda r: r.lap_time)

    def __str__(self) -> str:
        """Return a readable summary of the car."""
        driver_name = getattr(self.__driver, "name", None)
        driver_display = driver_name if driver_name is not None else str(self.__driver)
        return (
            f"{self.__model_year} {self.__team} "
            f"({self.__engine_maker}) - Driver: {driver_display}"
        )

    def __repr__(self) -> str:
        """Return a detailed string representation for debugging."""
        return (
            "Car("
            f"model_year={self.__model_year!r}, "
            f"team={self.__team!r}, "
            f"engine_maker={self.__engine_maker!r}, "
            f"driver={self.__driver!r}, "
            f"results={self.__results!r}"
            ")"
        )
