from race_manager import RaceManager
from nascar_data import NASCARData
from f1_data import F1Data
from indycar_data import IndyCarData

if __name__ == "__main__":
    # Create the manager
    manager = RaceManager()

    # Add different race types
    manager.add_race(NASCARData("Charlotte", 150))
    manager.add_race(F1Data("Spa", 44))
    manager.add_race(IndyCarData("Indy 500", 200))

    # List all races
    print("Listing all races and scores:")
    manager.list_races()

    # Print total score
    print("Total score:", manager.total_score())