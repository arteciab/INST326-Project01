"""
Data Importer Module
Handles importing racing data from CSV, JSON, and XML formats.
Converts external data into project class instances.
"""

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# Import your existing classes from the same folder
from car import Car
from analytics import Analytics
# Import other classes as needed (Race, Driver, etc.)


class DataImporter:
    """
    Centralized importer that converts external data files 
    into your project's OOP objects.
    """
    
    @staticmethod
    def import_races_csv(filepath):
        """
        Import races from CSV file and return list of Race objects.
        
        Args:
            filepath (str): Path to CSV file
            
        Returns:
            list: List of Race objects
            
        Example:
            races = DataImporter.import_races_csv('data/races.csv')
        """
        races = []
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create Race object (adjust based on your Race class constructor)
                # This is pseudocode - adjust to match your actual Race class
                race = {
                    'race_id': row.get('race_id'),
                    'name': row.get('name'),
                    'date': row.get('date'),
                    'location': row.get('location')
                }
                races.append(race)
        return races
    
    @staticmethod
    def import_races_json(filepath):
        """
        Import races from JSON file.
        
        Args:
            filepath (str): Path to JSON file
            
        Returns:
            list: List of Race objects
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        races = []
        for race_data in data.get('races', []):
            race = {
                'race_id': race_data.get('race_id'),
                'name': race_data.get('name'),
                'date': race_data.get('date'),
                'location': race_data.get('location')
            }
            races.append(race)
        return races
    
    @staticmethod
    def import_races_xml(filepath):
        """
        Import races from XML file.
        
        Args:
            filepath (str): Path to XML file
            
        Returns:
            list: List of Race objects
        """
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        races = []
        for race_elem in root.findall('race'):
            race = {
                'race_id': race_elem.find('race_id').text,
                'name': race_elem.find('name').text,
                'date': race_elem.find('date').text,
                'location': race_elem.find('location').text
            }
            races.append(race)
        return races
    
    @staticmethod
    def import_cars_csv(filepath):
        """Import cars from CSV file."""
        cars = []
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Adjust constructor parameters based on your Car class
                car = Car(
                    car_id=row['car_id'],
                    team=row['team'],
                    model=row.get('model', ''),
                    engine=row.get('engine', '')
                )
                cars.append(car)
        return cars
    
    @staticmethod
    def import_cars_json(filepath):
        """Import cars from JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cars = []
        for car_data in data.get('cars', []):
            car = Car(
                car_id=car_data['car_id'],
                team=car_data['team'],
                model=car_data.get('model', ''),
                engine=car_data.get('engine', '')
            )
            cars.append(car)
        return cars
    
    @staticmethod
    def auto_import(filepath, data_type='races'):
        """
        Automatically detect file format and import.
        
        Args:
            filepath (str): Path to data file
            data_type (str): Type of data ('races', 'cars', etc.)
            
        Returns:
            list: List of appropriate objects
            
        Example:
            races = DataImporter.auto_import('data/races.csv', 'races')
            cars = DataImporter.auto_import('data/cars.json', 'cars')
        """
        filepath = Path(filepath)
        extension = filepath.suffix.lower()
        
        importers = {
            'races': {
                '.csv': DataImporter.import_races_csv,
                '.json': DataImporter.import_races_json,
                '.xml': DataImporter.import_races_xml
            },
            'cars': {
                '.csv': DataImporter.import_cars_csv,
                '.json': DataImporter.import_cars_json
            }
        }
        
        if data_type not in importers:
            raise ValueError(f"Unknown data type: {data_type}")
        
        if extension not in importers[data_type]:
            raise ValueError(f"Unsupported format for {data_type}: {extension}")
        
        return importers[data_type][extension](str(filepath))


# Example usage if run directly
if __name__ == "__main__":
    # Test the importer
    print("Testing DataImporter...")
    
    # Example: Import races from CSV
    try:
        races = DataImporter.import_races_csv('../data/races.csv')
        print(f"Successfully loaded {len(races)} races")
    except Exception as e:
        print(f"Error: {e}")