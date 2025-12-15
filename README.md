# Checkered Data – Racing Analytics System

INST 326: Object-Oriented Programming  
Professor Dempy  
Team Repository: https://github.com/arteciab/INST326-Project01
Presentation Link: 
https://1drv.ms/v/c/577754f2f5b1f94d/IQAAi_GeaWRATrNPQaZTlqUiAZP7umSJVtA_KSyZAHuFDkQ?e=OeZ99q

## Overview
Checkered Data is a racing analytics system developed across four course projects. Each project builds directly on the previous one. We started with a standalone function library, transitioned into an object-oriented class system, added inheritance and polymorphism, and finalized the system with full integration, persistence, and testing. The final system is structured, maintainable, and designed to mirror real-world motorsport analytics workflows.

## Team Members and Roles
Artecia Brown – Core Data and Architecture  
Focus: base class design, data validation, retrieval logic  

Mory Camara – Analytics and Testing  
Focus: scoring logic, composition features, integration, and system testing  

Kevin Morales – Persistence and Integration  
Focus: save and load functionality, workflow integration, documentation  

**Note on Git Contributions**  
Due to local Git configuration differences, some commits appear under multiple usernames.  
Kevin Morales appears as `bevinborales` and `Kevin Morales`.  
Mory Camara appears as `MoryGit6` and `b0tMory`.

## Project 1: Racing Analytics Function Library
Project 1 established the foundation of the system. We created a reusable function library responsible for loading race and driver data, validating records, sorting and filtering results, calculating averages and comparisons, and generating basic summaries. These functions were intentionally written cleanly and modularly so they could later be converted into class methods.

## Project 2: Core Object-Oriented System
Project 2 converted the function library into a full class-based architecture. Core classes included RaceDataStore for loading and organizing race data, RaceAnalytics for statistical calculations, and ReportBuilder for formatted summaries. An optional NASCAR dataset (races_artecia.csv) was added with real drivers such as Rajah Caruth, Dale Earnhardt, and Leland Honeyman Jr. The system automatically works with either dataset without additional setup.

## Project 3: Inheritance, Polymorphism, and Composition
Project 3 introduced advanced object-oriented concepts. An abstract base class, AbstractRaceData, defines shared structure and enforces a required compute_performance_score method. Three subclasses inherit from it: NASCARData, F1Data, and IndyCarData. Each subclass overrides the same method while calculating scores differently, demonstrating polymorphism. A RaceManager class demonstrates composition by managing collections of race objects, allowing races of different types to be stored together, listed, and combined into a total score.

## Project 4: Capstone Integration and Testing
Project 4 completed the system through full integration, persistence, and testing. The RaceManager supports saving and loading application state using JSON through to_dict, from_dict, save_to_file, and load_from_file. Integration tests confirm that race objects are reconstructed correctly and that scoring remains accurate after reload. System tests validate complete end-to-end workflows, including saving state, restarting the system, and continuing analysis without data loss. File operations handle missing files and invalid data safely.

## Project Structure
<pre>
INST326-Project01/
├── src/
│   ├── abstract_race_data.py
│   ├── nascar_data.py
│   ├── f1_data.py
│   ├── indycar_data.py
│   ├── race_manager.py
│   ├── persistence.py
│   ├── data_importer.py
│   ├── datastore.py
│   ├── racing_library.py
│   ├── analytics.py
│   └── reporting.py

├── tests/
│   ├── test_inheritance_local.py
│   ├── polymorphism_test.py
│   ├── manager_test.py
│   ├── test_datastore.py
│   ├── test_driver_link.py
│   ├── test_racing_library.py
│   ├── test_integration_persistence.py
│   ├── test_integration_workflows.py
│   └── test_system_end_to_end.py

├── data/
│   ├── races.csv
│   └── races_artecia.csv

├── examples/
│   └── demo_script.py

├── README.md
├── requirements.txt
└── .gitignore
</pre>

## Testing

Testing spans Projects 2 through 4 and includes unit, integration, and system tests. Project 2 tests verify data loading, validation, searching, filtering, and sorting. Project 3 tests confirm inheritance structure, method overriding, polymorphic behavior, and composition through RaceManager. Project 4 tests confirm persistence, correct reconstruction of subclasses, score consistency, and full end-to-end workflows across restarts. All tests currently pass, confirming the system is stable.

## Running and Testing the Project

To run the test suite locally:

```bash
python -m pytest
```

## Credits

Team: Artecia Brown, Mory Camara, Kevin Morales
University of Maryland, College of Information Studies
