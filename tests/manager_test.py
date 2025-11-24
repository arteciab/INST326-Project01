import sys
import os

# Allow tests to import from src/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.race_manager import RaceManager
from src.nascar_data import NASCARData
from src.f1_data import F1Data
from src.indycar_data import IndyCarData

if __name__ == "__main__":
    manager = RaceManager()

    manager.add_race(NASCARData("Charlotte", 150))
    manager.add_race(F1Data("Spa", 44))
    manager.add_race(IndyCarData("Indy 500", 200))

    print("Listing all races and scores:")
    manager.list_races()

    print("Total score:", manager.total_score())
