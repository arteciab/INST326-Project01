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
