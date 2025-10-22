# Project 01 – Racing Analytics Function Library

**Course:** INST 326 – Object-Oriented Programming  
**Professor:** Dempy  
**Due Date:** October 12, 2025  
**Team Repository:** (https://github.com/arteciab/INST326-Project01)

---

## Project Overview

This project is a Python function library built to support **racing analytics**.  
It includes tools for loading, validating, analyzing, and reporting on race and driver data.

These functions were designed as **reusable components** that can later become class methods in Project 02.  
Together, they make it easier to manage motorsport data, including race results, driver performance, and team comparisons, in a clean, structured way.

---

## Team Members and Roles

| Name | Role | Focus Area |
|------|------|-------------|
| **Artecia** | Racing Library | Managing race and driver data |
| **Mory** | Analytics Library | Calculations and data validation |
| **Kevin** | Reporting Library | Summaries, comparisons, and saving reports |

---

## Domain Focus and Problem Statement

Racing events produce large amounts of data, driver names, lap times, race dates, team results, and more.  
Without organized tools, this information can be hard to manage and analyze.

Our goal was to create a **simple, well-structured Python function library** to help process racing data.  
It supports loading data, validating it, performing analytics, and producing formatted summaries that will be expanded into full classes in future projects.
Collaboration and Version Control

Each team member worked on their own module in separate branches.

Commits included clear messages describing the changes.

Pull requests were used for merging, with peer review required first.

Code followed PEP 8 style guidelines and used consistent docstring formatting.

Each member implemented 3–5 functions and reviewed at least one teammate’s code.

AI Collaboration

AI tools were used responsibly to help with:

Formatting docstrings

Debugging syntax and logic errors

Suggesting improvements to code clarity

All AI-assisted code was reviewed, tested, and modified by the team to ensure full understanding and accuracy.

Future Work

In Project 02, this library will be converted into an object-oriented design.
We’ll create classes such as Race, Driver, and Team, where these current functions become methods.
We also plan to expand analytics, reporting, and visualization features.


---

## Installation and Setup


```bash
git clone https://github.com/arteciab/INST326-Project01.git
cd INST326-Project01

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

docs/
├── function_reference.md
└── usage_examples.md

examples/
└── demo_script.py

src/
├── __init__.py
├── analytics.py
├── racing_library.py
├── reporting.py
└── utils.py

tests/
.gitignore
README.md
requirements.txt

from src.racing_library import load_race_data, sort_races_by_date, filter_by_team
from src.analytics import calculate_average_finish_from_file
from src.reporting import format_comparison_output, save_analysis_report

races = load_race_data("data/races.csv")
sorted_races = sort_races_by_date(races)

ferrari_results = filter_by_team(sorted_races, "Ferrari")

avg_time = calculate_average_finish_from_file("data/finish_times.txt")
print(f"Average Finish Time: {avg_time:.2f}")

driver1 = {"name": "Driver A", "starts": 10, "podiums": 4, "best_finish": 1, "finishes": [1, 4, 2]}
driver2 = {"name": "Driver B", "starts": 9, "podiums": 3, "best_finish": 2, "finishes": [2, 3, "DNF"]}

report_text = format_comparison_output(driver1, driver2)
save_path = save_analysis_report(report_text, "reports", "driver_comparison.md")
print(f"Report saved to: {save_path}")

| Category          | Example Functions                                                             | Description                                          |
| ----------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Data Handling** | `load_race_data`, `sort_races_by_date`, `filter_by_team`                      | Load, clean, and organize race and driver records.   |
| **Analytics**     | `calculate_average_finish`, `validate_driver_rows`                            | Perform calculations and data validation.            |
| **Reporting**     | `format_comparison_output`, `generate_driver_profile`, `save_analysis_report` | Create summaries, comparisons, and markdown reports. |
| **Utilities**     | Functions in `utils.py`                                                       | Shared helper functions used across modules.         |
