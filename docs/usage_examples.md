# Usage Examples

## Example 1 – Calculate average finish time
```python
from src.analytics import calculate_average_finish_from_file

avg = calculate_average_finish_from_file("data/finish_times.txt")
print("Average finish time:", round(avg, 2))
```

## Example 2 – Filter races by team
```python
from src.racing_library import load_race_data, filter_by_team

races = load_race_data("data/races.csv")
ferrari = filter_by_team(races, "Ferrari")
print("Ferrari races:", ferrari)
```

## Example 3 – Create a driver comparison report
```python
from src.reporting import format_comparison_output, save_analysis_report

driver1 = {"name": "Driver A", "starts": 10, "podiums": 4, "best_finish": 1, "finishes": [1, 2, 3]}
driver2 = {"name": "Driver B", "starts": 9, "podiums": 3, "best_finish": 2, "finishes": [2, 3, 'DNF']}

report = format_comparison_output(driver1, driver2)
path = save_analysis_report(report, "reports", "driver_comparison.md")
print("Saved to:", path)
```
