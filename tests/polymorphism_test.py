import sys
import os

# Allow tests to import from src/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nascar_data import NASCARData
from src.f1_data import F1Data
from src.indycar_data import IndyCarData

def show_scores():
    races = [
        NASCARData("Daytona", 200),
        F1Data("Monaco", 78),
        IndyCarData("Indy 500", 200)
    ]

    for r in races:
        print(f"Race type: {type(r).__name__}")
        print("Performance score:", r.compute_performance_score())
        print("-----")

if __name__ == "__main__":
    show_scores()
