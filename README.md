
---

# Checkered Data – Project 3: Advanced OOP

**Course:** INST 326 – Object-Oriented Programming
**Professor:** Dempy
**University:** University of Maryland

**Team Members:**
Artecia Brown
Mory Camara
Kevin Morales

---

## Project Overview

This project extends our existing racing analytics system by implementing inheritance, polymorphism, abstract base classes, and composition. The goal was to restructure our code so multiple race types could share a common interface while still behaving differently where appropriate.

---

## Inheritance and Abstract Base Class

We created an abstract base class called `AbstractRaceData` using Python’s `abc` module. This class defines shared attributes for all race types and enforces the required method `compute_performance_score()`.

Concrete subclasses including `NASCARData`, `F1Data`, and `IndyCarData` inherit from this base class and override the required method with race-specific logic. This represents a clear “is-a” relationship between race types.

---

## Polymorphism

Polymorphism is demonstrated through the `compute_performance_score()` method. The same method call produces different results depending on the race subclass. Higher-level code can work with race objects generically without needing to know their specific type.

---

## Composition

Composition is implemented through the `RaceManager` class. This class stores and manages a collection of race objects and performs operations such as listing races and calculating combined scores. Composition was chosen because a manager is not a type of race but instead operates on multiple races.

---

## Testing

Tests were written to verify:

* Abstract base class enforcement
* Correct method overriding in subclasses
* Polymorphic behavior across race types
* Proper behavior of the composition relationship

---

## Team Contributions

* **Artecia Brown:** Designed the abstract base class, race subclasses, and inheritance structure
* **Mory Camara:** Contributed to analytics logic and testing of polymorphic behavior
* **Kevin Morales:** Assisted with integration, documentation, and review of design decisions

---

## Collaboration

Each team member worked on a separate branch and merged changes through pull requests. All code was reviewed before merging. AI tools were used only for support and debugging, and all final code was written and understood by the team.

---

## File Structure

```
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
```

---

## Credits

Artecia Brown
Mory Camara
Kevin Morales

University of Maryland
Fall 2025

---

