from __future__ import annotations

from typing import Iterable, List, Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    # If you have real Driver/Result classes, these imports can be updated to match your project.
    from src.driver import Driver  # type: ignore
    from src.result import Result  # type: ignore


class Car:
    """
    Car supports two constructor styles so older project code and the new importer tests both work.

    Style A (your original style):
        Car(model_year=2025, team="Ferrari", engine_maker="Ferrari", driver=<Driver>, results=[<Result>])

    Style B (importer/tests style):
        Car(car_id="C001", team="Red Bull Racing", model="RB19", engine="Honda")
    """

    def __init__(
        self,
        model_year: Optional[int] = None,
        team: str = "",
        engine_maker: Optional[str] = None,
        driver: Optional[Any] = None,
        results: Optional[Iterable[Any]] = None,
        # Added for importer/tests:
        car_id: Optional[str] = None,
        model: Optional[str] = None,
        engine: Optional[str] = None,
    ):
        # Accept either engine_maker or engine (same concept)
        if engine_maker is None:
            engine_maker = engine

        # Store optional importer fields
        self.__car_id = car_id
        self.__model = model

        # Light validation (do not over-restrict so importer can create Car objects)
        if model_year is not None and not isinstance(model_year, int):
            raise TypeError("Model Year must be an int")
        if team is not None and not isinstance(team, str):
            raise TypeError("Team must be a string")
        if engine_maker is not None and not isinstance(engine_maker, str):
            raise TypeError("Engine Manufacturer must be a string")
        if car_id is not None and not isinstance(car_id, str):
            raise TypeError("car_id must be a string")
        if model is not None and not isinstance(model, str):
            raise TypeError("model must be a string")

        # Keep your original internal fields
        self.__model_year = model_year
        self.__team = team
        self.__engine_maker = engine_maker
        self.__driver = driver

        # Keep results behavior, but do not require a specific Result type at runtime
        self.__results: List[Any] = list(results) if results else []

    def get_car_details(self):
        """
        Return a summary of this Car's core metadata.
        """
        return {
            "Car ID": self.__car_id,
            "Team": self.__team,
            "Driver": self.__driver,
            "Engine maker": self.__engine_maker,
            "Model": self.__model,
            "Model year": self.__model_year,
        }

    @property
    def car_id(self) -> Optional[str]:
        return self.__car_id

    @property
    def model(self) -> Optional[str]:
        return self.__model

    @property
    def team(self) -> str:
        return self.__team

    @property
    def engine_maker(self) -> Optional[str]:
        return self.__engine_maker

    @property
    def model_year(self) -> Optional[int]:
        return self.__model_year

    @property
    def driver(self) -> Optional[Any]:
        return self.__driver

    @property
    def results(self):
        """
        Read-only view of this car's race results.
        """
        return tuple(self.__results)

    def add_result(self, result: Any):
        """
        Append a single race result to this car.

        We keep this flexible so it will not break if Result type is not imported here.
        """
        if result is None:
            raise TypeError("result must not be None")
        self.__results.append(result)

    def best_lap(self) -> Optional[Any]:
        """
        Return the result with the lowest lap_time for this car (if present).
        """
        if not self.__results:
            return None

        # Works if your Result objects have .lap_time
        return min(self.__results, key=lambda r: getattr(r, "lap_time"))

    def __str__(self) -> str:
        driver_name = getattr(self.__driver, "name", None)
        driver_display = driver_name if driver_name is not None else str(self.__driver)

        parts = []
        if self.__model_year is not None:
            parts.append(str(self.__model_year))
        if self.__team:
            parts.append(self.__team)
        if self.__model:
            parts.append(self.__model)
        if self.__engine_maker:
            parts.append(f"({self.__engine_maker})")

        base = " ".join(parts).strip() if parts else "Car"
        if self.__driver is not None:
            return f"{base} - Driver: {driver_display}"
        return base

    def __repr__(self) -> str:
        return (
            "Car("
            f"car_id={self.__car_id!r}, "
            f"model={self.__model!r}, "
            f"model_year={self.__model_year!r}, "
            f"team={self.__team!r}, "
            f"engine_maker={self.__engine_maker!r}, "
            f"driver={self.__driver!r}, "
            f"results={self.__results!r}"
            ")"
        )
