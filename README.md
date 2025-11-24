

# **Checkered Data – Racing Analytics System**

INST 326: Object Oriented Programming
Professor Dempy
Team Repository: [https://github.com/arteciab/INST326-Project01](https://github.com/arteciab/INST326-Project01)

---

## **Overview**

Checkered Data is a full racing analytics system that we have been building across four major projects. Each project was built on the last one. We started with basic functions, transitioned into an organized class system, added advanced object-oriented features, and then prepared for our final integration work for Project 4. Everything is structured, clean, and designed to feel realistic for motorsport analytics.

---

## **Team Members and Roles**

| Name              | Role                       | Focus Area                                          |
| ----------------- | -------------------------- | --------------------------------------------------- |
| **Artecia Brown** | Core Data and Architecture | Base class design, data validation, retrieval logic |
| **Mory Camara**   | Analytics and Testing      | Scoring logic, composition features, test scripts   |
| **Kevin Morales** | Reporting and Polymorphism | Subclass behavior, formatting, documentation        |

---

# **Project 1: Racing Analytics Function Library**

Project 1 was our starting point. We created a set of reusable functions that handled:

* loading race and driver data
* validating records
* sorting and filtering
* calculating averages and comparisons
* creating basic summaries

The point of this phase was to build a simple and clean functional library that we could later turn into full classes.

---

# **Project 2: Core Object-Oriented System**

Project 2 converted our entire function library into a class-based system.

We created:

* `RaceDataStore` for organizing and loading race data
* `RaceAnalytics` for calculations and statistics
* `ReportBuilder` for formatted summaries

We also added an optional NASCAR dataset (`races_artecia.csv`) that includes real drivers like Rajah Caruth, Dale Earnhardt, and Leland Honeyman Jr. Our system works with either dataset without any extra setup.

Each teammate took their section from Project 1 and rebuilt it as a class with properties, validation, string methods, and documentation.

---

# **Project 3: Inheritance, Polymorphism, and Composition**

This phase introduced advanced object-oriented programming.

---

## **Base Class Created by Artecia**

### `AbstractRaceData`

Defines the structure for all race types:

* race name
* number of laps

Requires each subclass to implement:

* `compute_performance_score()`

This keeps the system consistent and makes sure all race types follow the same basic rules.

---

## **Subclass Designs Created by Artecia and Kevin**

We built three race types that all inherit from the same parent class:

* **NASCARData**: score is laps times 1.2
* **F1Data**: score is laps times 2.5
* **IndyCarData**: score is laps times 1.8

All subclasses use the same method name, but they calculate the score differently. This demonstrates polymorphism.

---

## **Composition System Created by Mory**

### `RaceManager`

Handles storing and managing a group of race objects.

It can:

* store multiple race types
* add races
* list scores
* calculate a combined score

This shows a has a relationship and completes the advanced object oriented requirements.

---

# **Project 4: Final Integration and System Polish (Upcoming)**

Project 4 is due next month. This phase has not been completed yet.
Our plan for Project 4 includes:

* restructuring and polishing the full system
* adding higher-level tests
* improving documentation and diagrams
* integrating optional reporting and visualization upgrades
* preparing the final version of Checkered Data for submission

Projects 1 through 3 provide the foundation for this work.

---

# **Current Project Structure**

```
src/
├── abstract_race_data.py
├── nascar_data.py
├── f1_data.py
├── indycar_data.py
└── race_manager.py

tests/
├── test_inheritance_local.py
├── polymorphism_test.py
└── manager_test.py

data/
├── races.csv
└── races_artecia.csv
```

---

# **How to Run Tests**

```
python tests/test_inheritance_local.py
python tests/polymorphism_test.py
python tests/manager_test.py
```

All current tests pass and confirm:

* inheritance works
* subclasses override the required method
* Polymorphism behaves correctly
* Composition through the RaceManager works as expected

---

# **Future Feature Ideas**

* more race subclasses
* improved scoring and ranking models
* visuals and charts
* dashboards or UI tools
* larger datasets and real-world motorsport data

---

# **Credits**

Team: Artecia Brown, Mory Camara, Kevin Morales
University of Maryland, College of Information Studies

