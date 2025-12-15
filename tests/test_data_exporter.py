"""
Unit tests for DataExporter class.
Tests export functionality for CSV, JSON, XML, and reports.
"""

import unittest
import tempfile
import os
import csv
import json
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_exporter import DataExporter


class TestDataExporterCSV(unittest.TestCase):
    """Test CSV export functionality."""
    
    def setUp(self):
        """Create temporary directory and sample data."""
        self.test_dir = tempfile.mkdtemp()
        self.sample_races = [
            {'race_id': 'R001', 'name': 'Monaco GP', 'date': '2024-05-26', 'location': 'Monaco'},
            {'race_id': 'R002', 'name': 'Spanish GP', 'date': '2024-06-23', 'location': 'Barcelona'}
        ]
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_export_races_csv(self):
        """Test exporting races to CSV."""
        filepath = os.path.join(self.test_dir, 'races.csv')
        count = DataExporter.export_races_csv(self.sample_races, filepath)
        
        self.assertEqual(count, 2)
        self.assertTrue(os.path.exists(filepath))
        
        # Verify contents
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['name'], 'Monaco GP')
    
    def test_export_empty_list(self):
        """Test exporting empty list."""
        filepath = os.path.join(self.test_dir, 'empty.csv')
        count = DataExporter.export_races_csv([], filepath)
        
        self.assertEqual(count, 0)
        self.assertTrue(os.path.exists(filepath))


class TestDataExporterJSON(unittest.TestCase):
    """Test JSON export functionality."""
    
    def setUp(self):
        """Create temporary directory and sample data."""
        self.test_dir = tempfile.mkdtemp()
        self.sample_races = [
            {'race_id': 'R001', 'name': 'Monaco GP', 'date': '2024-05-26', 'location': 'Monaco'}
        ]
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_export_races_json(self):
        """Test exporting races to JSON."""
        filepath = os.path.join(self.test_dir, 'races.json')
        count = DataExporter.export_races_json(self.sample_races, filepath)
        
        self.assertEqual(count, 1)
        self.assertTrue(os.path.exists(filepath))
        
        # Verify contents
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.assertIn('races', data)
            self.assertEqual(len(data['races']), 1)
            self.assertEqual(data['races'][0]['name'], 'Monaco GP')


class TestDataExporterReports(unittest.TestCase):
    """Test report generation."""
    
    def setUp(self):
        """Create temporary directory and sample data."""
        self.test_dir = tempfile.mkdtemp()
        self.sample_race = {'race_id': 'R001', 'name': 'Monaco GP', 'date': '2024-05-26', 'location': 'Monaco'}
        self.sample_results = [
            {'race_id': 'R001', 'driver_id': 'D001', 'position': 1, 'points': 25},
            {'race_id': 'R001', 'driver_id': 'D002', 'position': 2, 'points': 18}
        ]
    
    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_export_race_summary_report(self):
        """Test exporting race summary report."""
        filepath = os.path.join(self.test_dir, 'race_report.txt')
        DataExporter.export_race_summary_report(self.sample_race, self.sample_results, filepath)
        
        self.assertTrue(os.path.exists(filepath))
        
        # Verify contents
        with open(filepath, 'r') as f:
            content = f.read()
            self.assertIn('RACE SUMMARY REPORT', content)
            self.assertIn('Monaco GP', content)
            self.assertIn('25 points', content)


if __name__ == '__main__':
    unittest.main(verbosity=2)