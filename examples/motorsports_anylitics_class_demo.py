from src.car_anylitics_class import MotorsportAnalytics
from pathlib import Path
import sys, os



tool = MotorsportAnalytics("data/races.csv")

print(tool)
# MotorsportAnalytics: 3 races loaded

print(tool.races_by_driver())
# {'Alice': 2, 'Bob': 1}

print(tool.races_by_team())
# {'Alpha': 2, 'Beta': 1}

print(tool.driver_circuits("Alice"))
# ['Bahrain', 'Melbourne']

print(tool.races_timeline())
# [('2024-01-20', 'Monaco'), ('2024-02-01', 'Bahrain'), ('2024-03-10', 'Melbourne')]

