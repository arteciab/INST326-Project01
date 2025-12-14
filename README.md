Checkered Data – Project 3: Advanced OOP

Course: INST 326 – Object-Oriented Programming
Professor: Dempy
University: University of Maryland

Team Members:
Artecia Brown
Mory Camara
Kevin Morales

Project Overview

This project extends our existing racing analytics system by implementing inheritance, polymorphism, abstract base classes, and composition. The goal was to restructure our code so multiple race types could share a common interface while still behaving differently where appropriate.

Inheritance and Abstract Base Class

We created an abstract base class called AbstractRaceData using Python’s abc module. This class defines shared attributes for all race types and enforces the required method compute_performance_score().

Concrete subclasses, including NASCARData, F1Data, and IndyCarData, inherit from this base class and override the required method with race-specific logic. This represents a clear “is-a” relationship between race types.

Polymorphism

Polymorphism is demonstrated through the compute_performance_score() method. The same method call produces different results depending on the race subclass. Higher-level code can work with race objects generically without needing to know their specific type.

Composition

Composition is implemented through the RaceManager class. This class stores and manages a collection of race objects and performs operations such as listing races and calculating combined scores. Composition was chosen because a manager is not a type of race but instead operates on multiple races.

Testing

Tests were written to verify:

Abstract base class enforcement

Correct method overriding in subclasses

Polymorphic behavior across race types

Proper behavior of the composition relationship

Team Contributions

Artecia Brown: Designed the abstract base class, race subclasses, and inheritance structure

Mory Camara: Contributed to analytics logic and testing of polymorphic behavior

Kevin Morales: Assisted with integration, documentation, and review of design decisions

Collaboration

Each team member worked on a separate branch and merged changes through pull requests. All code was reviewed before merging. AI tools were used only for support and debugging, and all final code was written and understood by the team.

File Structure
src/
├── abstract_race_data.py
├── nascar_data.py
├── f1_data.py
├── indycar_data.py
├── race_manager.py

tests/
├── test_inheritance_local.py
├── polymorphism_test.py
├── manager_test.py

Credits

Artecia Brown
Mory Camara
Kevin Morales

University of Maryland
Fall 2025
- All code was reviewed before merging to keep the repo stable.  
- Commits used short, clear messages.  
- Followed PEP 8 style for consistency and readability.  
- Each teammate implemented 3–5 methods and reviewed one peer’s work.  

---

## AI Collaboration

AI tools were used for formatting, debugging, and syntax checks. All final code was reviewed and rewritten by the team.


---

## Installation and Setup

```bash
git clone https://github.com/arteciab/INST326-Project01.git
cd INST326-Project01

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## File Structure

```text
docs/
├── function_reference.md
├── usage_examples.md
└── class_design.md

examples/
└── demo_script.py

src/
├── __init__.py
├── analytics.py
├── datastore.py
├── reporting.py
└── utils.py

data/
├── races.csv
└── races_artecia.csv

tests/
├── test_datastore.py
├── test_driver_link.py
└── test_racing_library.py

test_my_class.py
.gitignore
README.md
requirements.txt

## Usage Example

```python
from src.datastore import RaceDataStore
from src.analytics import RaceAnalytics
from src.reporting import ReportBuilder

store = RaceDataStore()
count = store.load_race_data("data/races_artecia.csv")
print("Loaded rows:", count)

print("\nAll Races (Newest First):")
for race in store.sort_races_by_date(ascending=False):
    print(f"{race.race_id}: {race.driver.name} - {race.team}")

print("\nDriver Profiles Created:")
for driver in store.list_driver_profiles():
    print(driver)

print("\nSearch Results for 'Dale Earnhardt':")
results = store.search_driver_results("Dale Earnhardt")
for r in results:
    print(f"{r.race_id}: {r.driver.name} - {r.team}")

analytics = RaceAnalytics(store)
report = ReportBuilder(store)

print("\nAverage Finish for Dale Earnhardt:")
print(analytics.average_finish_for_driver("Dale Earnhardt"))

print("\nDriver Summary:")
print(report.driver_summary("Dale Earnhardt"))

print("\nTeam Summary:")
print(report.team_summary("JR Motorsports"))

## Future Work
Next, we plan to make new versions of our classes for different types of races and add simple charts to show driver and team results.

## Credits
Team: Artecia Brown, Mory Camara, Kevin Morales  
University of Maryland – College of Information Studies, Fall 2025


