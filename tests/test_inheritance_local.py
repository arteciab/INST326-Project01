import sys
import os

# Add the project root to Python's path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nascar_data import NASCARData

# Create a NASCAR race object
race = NASCARData("Talladega 500", 188)

print("Race name:", race._race_name)
print("Laps:", race._laps)
print("Performance score:", race.compute_performance_score())
