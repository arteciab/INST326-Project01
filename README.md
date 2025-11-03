# Project 02 – Racing Analytics OOP System

**Course:** INST 326 – Object-Oriented Programming  
**Professor:** Dempy  
**Due Date:** November 2, 2025  
**Team Repository:** (https://github.com/arteciab/INST326-Project01)

---

## Project Overview

This project expands on our Project 1 function library by turning it into a full **object-oriented system** for racing analytics.  
We used Python classes to handle racing data, including races, drivers, and teams, with encapsulation, validation, and documentation built in.  

The goal was to make a program that’s organized, easy to update, and realistic to how motorsport analytics systems actually work.  
The project now supports both the team’s shared dataset and an optional NASCAR dataset for more authentic examples.

---

## Team Members and Roles

| Name | Role | Focus Area |
|------|------|-------------|
| **Artecia Brown** | Core Data & Retrieval Developer | Data access, organization, and validation |
| **Mory Camara** | Analytics & Testing Developer | Data analysis, performance comparison, and trend detection |
| **Kevin Morales** | Reporting & Integration Developer | Data formatting, visualization prep, and documentation |

---

### Team Contributions

- **Artecia Brown:** Built the `RaceDataStore` class to load, check, and organize racing data. Added an optional dataset (`data/races_artecia.csv`) with real NASCAR drivers like **Rajah Caruth**, **Leland Honeyman Jr.**, and **Dale Earnhardt** to make examples feel more realistic.  
  The code automatically detects that file if it exists but still works with the team’s main dataset (`data/races.csv`) without any extra setup.  

- **Mory Camara:** Created the analytics and performance comparison tools, including average finish calculations, team points, and podium statistics. Also wrote tests to make sure analytics functions run accurately and efficiently.  

- **Kevin Morales:** Focused on reporting and integration, building methods to format results, generate driver summaries, and create example outputs for documentation. Combined all modules into a working end-to-end system.  

---

## Domain Focus and Problem Statement

Racing events create huge amounts of data — race IDs, driver names, lap times, race dates, teams, and more.  
Without structure, that data is hard to search through or analyze.

Our system fixes that by giving users an organized way to load and compare race data.  
It supports searching by driver or team, sorting results by date, and summarizing overall performance trends.  
Using real NASCAR drivers made the final outputs feel closer to real-world use cases.

---

## Collaboration and Version Control

- Each team member worked on their own branch and merged through pull requests.  
- All code was reviewed before merging to keep the repo stable.  
- Commits used short, clear messages.  
- Followed PEP 8 style for consistency and readability.  
- Each teammate implemented 3–5 methods and reviewed one peer’s work.  

---

## AI Collaboration

AI tools were used for Formatting, debugging, and syntax checks. All Final code was reviewed amd rewritte by the team.


---

## Installation and Setup

```bash
git clone https://github.com/arteciab/INST326-Project01.git
cd INST326-Project01

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

## File Structure
docs/
├── function_reference.md
└── usage_examples.md

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
└── races_artecia.csv   ← optional NASCAR dataset

tests/
├── test_datastore.py
└── other test files...

test_my_class.py
.gitignore
README.md
requirements.txt

## Usage Example
from src.datastore import RaceDataStore

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


## Future Work
Next, we plan to make new versions of our classes for different types of races and add simple charts to show driver and team results.

## Credits
Team: Artecia Brown, Mory Camara, Kevin Morales  
University of Maryland – College of Information Studies, Fall 2025


