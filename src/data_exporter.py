"""
Demo script showing data export capabilities.
"""

import sys
sys.path.append('../src')

from data_exporter import DataExporter
from data_importer import DataImporter

def main():
    print("=" * 60)
    print("Racing Data Export Demo")
    print("=" * 60)
    
    # 1. Create sample data
    sample_races = [
        {'race_id': 'R001', 'name': 'Monaco GP', 'date': '2024-05-26', 'location': 'Monaco'},
        {'race_id': 'R002', 'name': 'Spanish GP', 'date': '2024-06-23', 'location': 'Barcelona'},
        {'race_id': 'R003', 'name': 'Canadian GP', 'date': '2024-06-09', 'location': 'Montreal'}
    ]
    
    sample_drivers = [
        {'driver_id': 'D001', 'name': 'Max Verstappen', 'team': 'Red Bull Racing', 'number': 1},
        {'driver_id': 'D002', 'name': 'Lewis Hamilton', 'team': 'Mercedes', 'number': 44}
    ]
    
    sample_results = [
        {'race_id': 'R001', 'driver_id': 'D001', 'position': 1, 'points': 25},
        {'race_id': 'R001', 'driver_id': 'D002', 'position': 2, 'points': 18},
        {'race_id': 'R002', 'driver_id': 'D001', 'position': 1, 'points': 25},
        {'race_id': 'R002', 'driver_id': 'D002', 'position': 3, 'points': 15}
    ]
    
    # 2. Export to different formats
    print("\n1. Exporting races to CSV...")
    count = DataExporter.export_races_csv(sample_races, '../data/output/races_export.csv')
    print(f"   ✓ Exported {count} races to CSV")
    
    print("\n2. Exporting drivers to JSON...")
    count = DataExporter.export_drivers_json(sample_drivers, '../data/output/drivers_export.json')
    print(f"   ✓ Exported {count} drivers to JSON")
    
    print("\n3. Exporting races to XML...")
    count = DataExporter.export_races_xml(sample_races, '../data/output/races_export.xml')
    print(f"   ✓ Exported {count} races to XML")
    
    print("\n4. Exporting results to CSV...")
    count = DataExporter.export_results_csv(sample_results, '../data/output/results_export.csv')
    print(f"   ✓ Exported {count} results to CSV")
    
    # 3. Generate reports
    print("\n5. Generating race summary report...")
    DataExporter.export_race_summary_report(
        sample_races[0], 
        [r for r in sample_results if r['race_id'] == 'R001'],
        '../data/output/monaco_report.txt'
    )
    print("   ✓ Generated race summary report")
    
    print("\n6. Generating driver statistics report...")
    driver_results = [r for r in sample_results if r['driver_id'] == 'D001']
    DataExporter.export_driver_statistics_report(
        sample_drivers[0],
        driver_results,
        '../data/output/driver_stats.txt'
    )
    print("   ✓ Generated driver statistics report")
    
    print("\n7. Generating championship standings report...")
    DataExporter.export_season_standings_report(
        sample_drivers,
        sample_results,
        '../data/output/championship_standings.txt'
    )
    print("   ✓ Generated championship standings report")
    
    # 4. Auto-export (format detection)
    print("\n8. Using auto-export with format detection...")
    DataExporter.auto_export(sample_races, '../data/output/auto_races.csv', 'races')
    DataExporter.auto_export(sample_drivers, '../data/output/auto_drivers.json', 'drivers')
    print("   ✓ Auto-exported data with format detection")
    
    print("\n" + "=" * 60)
    print("Export complete! Check the 'data/output/' folder.")
    print("=" * 60)

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    import os
    os.makedirs('../data/output', exist_ok=True)
    main()