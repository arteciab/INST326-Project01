# Usage Examples

## Example 1 – Calculate average finish time
```python
from src.analytics import calculate_average_finish_from_file
avg = calculate_average_finish_from_file("data/finish_times.txt")
print("Average finish time:", round(avg, 2))
