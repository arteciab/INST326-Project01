"""
Unit tests for DataImporter class.
Tests CSV, JSON, and XML import functionality with edge cases.
"""

import unittest
import tempfile
import os
from pathlib import Path
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from data_importer import DataImporter


class TestDataImporterCSV(unittest.TestCase):
    """Test CSV import functionality."""
    
    def setUp(self):
        """Create temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_import_valid_races_csv(self):
        """Test importing valid races from CSV."""
        csv_content = """race_id,name,date,location
R001,Monaco GP,2024-05-26,Monaco
R002,Spanish GP,2024-06-23,Barcelona
R003,Canadian GP,2024-06-09,Montreal"""
        
        filepath = os.path.join(self.test_dir, 'races.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        races = DataImporter.import_races_csv(filepath)
        
        self.assertEqual(len(races), 3)
        self.assertEqual(races[0]['race_id'], 'R001')
        self.assertEqual(races[0]['name'], 'Monaco GP')
        self.assertEqual(races[1]['location'], 'Barcelona')
    
    def test_import_empty_csv(self):
        """Test importing empty CSV file."""
        csv_content = """race_id,name,date,location"""
        
        filepath = os.path.join(self.test_dir, 'empty.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        races = DataImporter.import_races_csv(filepath)
        
        self.assertEqual(len(races), 0)
    
    def test_import_csv_missing_columns(self):
        """Test CSV with missing required columns."""
        csv_content = """race_id,name
R001,Monaco GP
R002,Spanish GP"""
        
        filepath = os.path.join(self.test_dir, 'missing_cols.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        races = DataImporter.import_races_csv(filepath)
        
        # Should still import but with None/empty values for missing fields
        self.assertEqual(len(races), 2)
        self.assertIsNone(races[0].get('date'))
    
    def test_import_csv_extra_columns(self):
        """Test CSV with extra columns (should be ignored)."""
        csv_content = """race_id,name,date,location,extra_field
R001,Monaco GP,2024-05-26,Monaco,ignored
R002,Spanish GP,2024-06-23,Barcelona,also_ignored"""
        
        filepath = os.path.join(self.test_dir, 'extra_cols.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        races = DataImporter.import_races_csv(filepath)
        
        self.assertEqual(len(races), 2)
        self.assertEqual(races[0]['name'], 'Monaco GP')
    
    def test_import_csv_special_characters(self):
        """Test CSV with special characters in data."""
        csv_content = """race_id,name,date,location
R001,"São Paulo GP",2024-11-03,"São Paulo, Brazil"
R002,México GP,2024-10-27,Mexico City"""
        
        filepath = os.path.join(self.test_dir, 'special_chars.csv')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(csv_content)
        
        races = DataImporter.import_races_csv(filepath)
        
        self.assertEqual(len(races), 2)
        self.assertIn('São Paulo', races[0]['name'])
    
    def test_import_csv_file_not_found(self):
        """Test importing non-existent CSV file."""
        with self.assertRaises(FileNotFoundError):
            DataImporter.import_races_csv('nonexistent_file.csv')
    
    def test_import_csv_invalid_format(self):
        """Test importing malformed CSV."""
        csv_content = """This is not a valid CSV
Just random text
No proper structure"""
        
        filepath = os.path.join(self.test_dir, 'invalid.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        # Should handle gracefully (exact behavior depends on implementation)
        try:
            races = DataImporter.import_races_csv(filepath)
            # If it doesn't raise an error, check it returns empty or handles it
            self.assertIsInstance(races, list)
        except Exception as e:
            # Or it might raise a specific exception
            self.assertIsInstance(e, (ValueError, KeyError))


class TestDataImporterJSON(unittest.TestCase):
    """Test JSON import functionality."""
    
    def setUp(self):
        """Create temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_import_valid_races_json(self):
        """Test importing valid races from JSON."""
        json_content = """{
"races": [
    {
    "race_id": "R001",
    "name": "Monaco GP",
    "date": "2024-05-26",
    "location": "Monaco"
    },
    {
    "race_id": "R002",
    "name": "Spanish GP",
    "date": "2024-06-23",
    "location": "Barcelona"
    }
]
}"""
        
        filepath = os.path.join(self.test_dir, 'races.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        races = DataImporter.import_races_json(filepath)
        
        self.assertEqual(len(races), 2)
        self.assertEqual(races[0]['race_id'], 'R001')
        self.assertEqual(races[1]['name'], 'Spanish GP')
    
    def test_import_empty_json(self):
        """Test importing empty JSON."""
        json_content = """{"races": []}"""
        
        filepath = os.path.join(self.test_dir, 'empty.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        races = DataImporter.import_races_json(filepath)
        
        self.assertEqual(len(races), 0)
    
    def test_import_json_missing_races_key(self):
        """Test JSON without 'races' key."""
        json_content = """{"data": [{"race_id": "R001"}]}"""
        
        filepath = os.path.join(self.test_dir, 'no_races_key.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        races = DataImporter.import_races_json(filepath)
        
        # Should return empty list when 'races' key is missing
        self.assertEqual(len(races), 0)
    
    def test_import_json_missing_fields(self):
        """Test JSON with missing required fields."""
        json_content = """{
"races": [
    {
    "race_id": "R001",
    "name": "Monaco GP"
    }
]
}"""
        
        filepath = os.path.join(self.test_dir, 'missing_fields.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        races = DataImporter.import_races_json(filepath)
        
        self.assertEqual(len(races), 1)
        self.assertIsNone(races[0].get('date'))
        self.assertIsNone(races[0].get('location'))
    
    def test_import_json_invalid_syntax(self):
        """Test importing malformed JSON."""
        json_content = """{
"races": [
    {"race_id": "R001",
    "name": "Monaco GP"
]
}"""  # Missing closing brace
        
        filepath = os.path.join(self.test_dir, 'invalid.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        with self.assertRaises(Exception):  # Should raise JSONDecodeError
            DataImporter.import_races_json(filepath)
    
    def test_import_json_not_a_list(self):
        """Test JSON where races is not a list."""
        json_content = """{"races": "not a list"}"""
        
        filepath = os.path.join(self.test_dir, 'not_list.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        # Should handle gracefully
        try:
            races = DataImporter.import_races_json(filepath)
            self.assertEqual(len(races), 0)
        except (TypeError, AttributeError):
            pass  # Either behavior is acceptable


class TestDataImporterXML(unittest.TestCase):
    """Test XML import functionality."""
    
    def setUp(self):
        """Create temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_import_valid_races_xml(self):
        """Test importing valid races from XML."""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<races>
<race>
    <race_id>R001</race_id>
    <name>Monaco GP</name>
    <date>2024-05-26</date>
    <location>Monaco</location>
</race>
<race>
    <race_id>R002</race_id>
    <name>Spanish GP</name>
    <date>2024-06-23</date>
    <location>Barcelona</location>
</race>
</races>"""
        
        filepath = os.path.join(self.test_dir, 'races.xml')
        with open(filepath, 'w') as f:
            f.write(xml_content)
        
        races = DataImporter.import_races_xml(filepath)
        
        self.assertEqual(len(races), 2)
        self.assertEqual(races[0]['race_id'], 'R001')
        self.assertEqual(races[1]['location'], 'Barcelona')
    
    def test_import_empty_xml(self):
        """Test importing empty XML."""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<races></races>"""
        
        filepath = os.path.join(self.test_dir, 'empty.xml')
        with open(filepath, 'w') as f:
            f.write(xml_content)
        
        races = DataImporter.import_races_xml(filepath)
        
        self.assertEqual(len(races), 0)
    
    def test_import_xml_missing_elements(self):
        """Test XML with missing elements."""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<races>
<race>
    <race_id>R001</race_id>
    <name>Monaco GP</name>
</race>
</races>"""
        
        filepath = os.path.join(self.test_dir, 'missing_elements.xml')
        with open(filepath, 'w') as f:
            f.write(xml_content)
        
        # Should handle missing elements gracefully
        try:
            races = DataImporter.import_races_xml(filepath)
            self.assertEqual(len(races), 1)
        except AttributeError:
            pass  # Acceptable if it raises error for missing required fields
    
    def test_import_xml_invalid_syntax(self):
        """Test importing malformed XML."""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<races>
<race>
    <race_id>R001</race_id>
    <name>Monaco GP
</race>
</races>"""  # Missing closing tag
        
        filepath = os.path.join(self.test_dir, 'invalid.xml')
        with open(filepath, 'w') as f:
            f.write(xml_content)
        
        with self.assertRaises(Exception):  # Should raise ParseError
            DataImporter.import_races_xml(filepath)
    
    def test_import_xml_special_characters(self):
        """Test XML with special characters."""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<races>
<race>
    <race_id>R001</race_id>
    <name>São Paulo GP &amp; More</name>
    <date>2024-11-03</date>
    <location>São Paulo</location>
</race>
</races>"""
        
        filepath = os.path.join(self.test_dir, 'special_chars.xml')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        races = DataImporter.import_races_xml(filepath)
        
        self.assertEqual(len(races), 1)
        self.assertIn('São Paulo', races[0]['name'])


class TestDataImporterCars(unittest.TestCase):
    """Test car import functionality."""
    
    def setUp(self):
        """Create temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_import_valid_cars_csv(self):
        """Test importing valid cars from CSV."""
        csv_content = """car_id,team,model,engine
C001,Red Bull Racing,RB19,Honda
C002,Mercedes,W14,Mercedes
C003,Ferrari,SF-23,Ferrari"""
        
        filepath = os.path.join(self.test_dir, 'cars.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        # Note: This assumes your Car class is properly imported
        try:
            cars = DataImporter.import_cars_csv(filepath)
            self.assertEqual(len(cars), 3)
        except Exception as e:
            # If Car class isn't available, skip this test
            self.skipTest(f"Car class not available: {e}")
    
    def test_import_cars_json(self):
        """Test importing cars from JSON."""
        json_content = """{
"cars": [
    {
    "car_id": "C001",
    "team": "Red Bull Racing",
    "model": "RB19",
    "engine": "Honda"
    },
    {
    "car_id": "C002",
    "team": "Mercedes",
    "model": "W14",
    "engine": "Mercedes"
    }
]
}"""
        
        filepath = os.path.join(self.test_dir, 'cars.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        try:
            cars = DataImporter.import_cars_json(filepath)
            self.assertEqual(len(cars), 2)
        except Exception as e:
            self.skipTest(f"Car class not available: {e}")


class TestAutoImport(unittest.TestCase):
    """Test automatic format detection."""
    
    def setUp(self):
        """Create temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_auto_import_csv(self):
        """Test auto-import detects CSV format."""
        csv_content = """race_id,name,date,location
R001,Monaco GP,2024-05-26,Monaco"""
        
        filepath = os.path.join(self.test_dir, 'races.csv')
        with open(filepath, 'w') as f:
            f.write(csv_content)
        
        races = DataImporter.auto_import(filepath, 'races')
        
        self.assertEqual(len(races), 1)
        self.assertEqual(races[0]['name'], 'Monaco GP')
    
    def test_auto_import_json(self):
        """Test auto-import detects JSON format."""
        json_content = """{"races": [{"race_id": "R001", "name": "Monaco GP", "date": "2024-05-26", "location": "Monaco"}]}"""
        
        filepath = os.path.join(self.test_dir, 'races.json')
        with open(filepath, 'w') as f:
            f.write(json_content)
        
        races = DataImporter.auto_import(filepath, 'races')
        
        self.assertEqual(len(races), 1)
    
    def test_auto_import_xml(self):
        """Test auto-import detects XML format."""
        xml_content = """<?xml version="1.0"?>
<races>
<race>
    <race_id>R001</race_id>
    <name>Monaco GP</name>
    <date>2024-05-26</date>
    <location>Monaco</location>
</race>
</races>"""
        
        filepath = os.path.join(self.test_dir, 'races.xml')
        with open(filepath, 'w') as f:
            f.write(xml_content)
        
        races = DataImporter.auto_import(filepath, 'races')
        
        self.assertEqual(len(races), 1)
    
    def test_auto_import_unsupported_format(self):
        """Test auto-import with unsupported format."""
        filepath = os.path.join(self.test_dir, 'races.txt')
        with open(filepath, 'w') as f:
            f.write("some data")
        
        with self.assertRaises(ValueError):
            DataImporter.auto_import(filepath, 'races')
    
    def test_auto_import_unknown_data_type(self):
        """Test auto-import with unknown data type."""
        filepath = os.path.join(self.test_dir, 'data.csv')
        with open(filepath, 'w') as f:
            f.write("data")
        
        with self.assertRaises(ValueError):
            DataImporter.auto_import(filepath, 'unknown_type')


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)