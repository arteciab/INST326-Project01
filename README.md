Project 01 – Racing Analytics Function Library

Course: INST 326 – Object-Oriented Programming
Professor Dempy
October 12, 2025
Team Repository: https://github.com/arteciab/INST326-Project01

Project Overview

This project is a Python function library designed to support racing analytics. It includes tools for loading, validating, analyzing, and reporting race and driver data. The functions were developed as reusable components that can later be turned into methods within classes for future projects. Together, these utilities make it easier to manage motorsport data such as race results, driver performance, and team comparisons.

| Name      | Role              | Focus Area                                 |
| --------- | ----------------- | ------------------------------------------ |
| Artecia   | Racing Library    | Managing race and driver data              |
| Mory      | Analytics Library | Calculations and data validation           |
| Kevin     | Reporting Library | Summaries, comparisons, and saving reports |

Domain Focus and Problem Statement

Racing events generate large amounts of data, including driver names, lap times, race dates, and team results. Managing and analyzing this information can be difficult without organized tools. Our project focuses on creating a simple Python function library that helps with data loading, validation, and analysis for racing performance. These functions make it easier to calculate statistics, compare results, and prepare data for reports or future object-oriented programs.

git clone https://github.com/arteciab/INST326-Project01.git
cd INST326-Project01

python -m venv venv
source venv/bin/activate      # Mac/Linux  
venv\Scripts\activate         # Windows

pip install -r requirements.txt

python examples/demo_script.py

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
├── utils.py
└── project1
tests/
.gitignore
README.md
requirements.txt

from src.racing_library import load_race_data, sort_races_by_date, filter_records_by_team
from src.analytics import calculate_average_finish
from src.reporting import format_comparison_output, save_analysis_report

# 1) Load and sort race data
races = load_race_data("data/races.csv")
sorted_races = sort_races_by_date(races)

# 2) Filter by team
ferrari_results = filter_records_by_team(sorted_races, "Ferrari")

# 3) Calculate average finish time
avg_time = calculate_average_finish("data/finish_times.txt")
print(f"Average Finish Time: {avg_time:.2f}")

# 4) Compare two drivers and save a report
driver1 = {"name": "Driver A", "starts": 10, "podiums": 4, "best_finish": 1, "finishes": [1, 4, 2]}
driver2 = {"name": "Driver B", "starts": 9, "podiums": 3, "best_finish": 2, "finishes": [2, 3, "DNF"]}
report_text = format_comparison_output(driver1, driver2)
save_path = save_analysis_report(report_text, "reports", "driver_comparison.md")
print(f"Report saved to: {save_path}")

| Category      | Example Functions                                                             | Description                                    |
| ------------- | ----------------------------------------------------------------------------- | ---------------------------------------------- |
| Data Handling | `load_race_data`, `sort_races_by_date`, `filter_records_by_team`              | Load, clean, and organize race/driver records. |
| Analytics     | `calculate_average_finish`, `validate_data_sources_min`                       | Perform basic calculations and validation.     |
| Reporting     | `format_comparison_output`, `generate_driver_profile`, `save_analysis_report` | Create summaries, comparisons, and reports.    |
| Utilities     | Functions in `utils.py`                                                       | Shared helper functions used across modules.   |

Collaboration and Version Control

Each team member worked on their own module in separate branches.

Code was committed with clear messages and merged using pull requests.

All code followed PEP 8 style guidelines and used consistent docstring formatting.

Each member implemented 3–5 functions and reviewed at least one teammate’s code.

AI Collaboration

AI tools were used to help format docstrings, identify errors, and suggest code improvements. All AI-assisted code was reviewed and tested by the team before submission to ensure understanding and accuracy.

Future Work

In Project 02, this library will be converted into an object-oriented design with classes such as Race, Driver, and Team. These classes will integrate the current functions as methods and expand on analytics and reporting features.
