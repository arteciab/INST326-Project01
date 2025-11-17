# Class Design Document  
Project 02 – Racing Analytics OOP System  
Team: Artecia Brown, Mory Camara, Kevin Morales  
Course: INST 326 – Fall 2025

---

## Overview

This document explains the design decisions behind the main classes we built for Project 02. Our goal was to take the core functions from Project 01 and turn them into a structured, object-oriented system that is easier to maintain, extend, and understand. Each class follows clear responsibilities, proper encapsulation, and consistent validation.

---

## 1. RaceDataStore

### Purpose
RaceDataStore is the central data manager for the entire system. It loads race data, validates fields, creates driver objects, and provides organized ways to search and filter information.

### Why This Design
- Keeps all race data in one controlled place.
- Prevents duplicated logic across the project.
- Provides a clear API for analytics and reporting classes.
- Makes the dataset consistent through validation.

### Key Features
- Loads CSV data with validation.
- Wraps race and driver data into dataclasses.
- Stores results in a private attribute.
- Offers search by driver or team.
- Sorts races by date.
- Builds a dictionary of unique drivers.

---

## 2. RaceAnalytics

### Purpose
RaceAnalytics handles all performance calculations. It turns raw results from RaceDataStore into useful metrics.

### Why This Design
Separating analytics from data storage keeps responsibilities clean. RaceDataStore manages data. RaceAnalytics analyzes it.

### Key Features
- Average finish calculations.
- Team performance summaries.
- Integration with Project 01 functions.
- Graceful handling of missing data.

---

## 3. ReportBuilder

### Purpose
ReportBuilder formats output into readable summaries and reports. It focuses on presentation, not calculations.

### Why This Design
Putting formatting in its own class prevents clutter in analytics and datastore logic. It also makes the system easier to extend.

### Key Features
- Driver summaries.
- Team summaries.
- Driver comparisons.
- Race summaries sorted by finishing position.

---

## 4. Dataclasses: Driver and RaceResult

### Purpose
These dataclasses store structured information: one for drivers and one for individual race results.

### Why This Design
Dataclasses reduce boilerplate and keep fields organized. They also make debugging and testing easier since values are explicit.

### Key Features
- Driver: id, name, team, optional nationality.
- RaceResult: race id, date, driver, team, position.

---

## 5. Encapsulation and Validation

### Encapsulation
We used private attributes where necessary (like `_results`) to prevent accidental modification outside the class.

### Validation
The system validates:
- missing or empty fields
- non-numeric finish times
- invalid dates
- invalid driver fields

This ensures data remains clean and prevents downstream errors.

---

## 6. Integration of Project 01 Functions

Instead of rewriting Project 01 functions, we converted them into methods inside the new classes:

- File loading functions → RaceDataStore
- Average finish → RaceAnalytics
- Summary formatting → ReportBuilder

This matches Project 02 requirements while keeping logic consistent.

---

## 7. Class Interactions

- RaceDataStore provides structured data to RaceAnalytics.
- RaceAnalytics computes performance metrics.
- ReportBuilder formats those metrics and results into readable output.

This structure makes the system easy to extend for Project 03.

---

## 8. Strengths of This Design

- Easy to maintain and understand.
- Clean separation of responsibilities.
- Fully compatible with future inheritance requirements.
- Works with multiple datasets.
- Passes all tests in the repository.

---
