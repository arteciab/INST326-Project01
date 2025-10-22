# Function Reference

## analytics.py
- **load_finish_times(path)** – reads numeric finish times from a text file.
- **calculate_average_finish_from_file(path)** – reads times and returns the average.
- **calculate_average_finish(times)** – returns the average of a list of numbers.
- **validate_driver_rows(rows)** – checks CSV-style driver rows for valid names/times.

## racing_library.py
- **load_race_data(source)** – loads race records from CSV/JSON or list.
- **validate_driver_record(record)** – checks one record for valid driver/team fields.
- **search_driver_results(data, driver_name)** – finds records matching a driver name.
- **filter_by_team(data, team_name)** – returns only records for a given team.
- **sort_races_by_date(data)** – sorts races by date, oldest to newest.

## reporting.py
- **format_race_summary(race, results, drivers_by_id)** – makes a markdown race summary.
- **generate_driver_profile(driver_id, all_results, drivers_by_id)** – builds a stats summary for one driver.
- **format_comparison_output(driver1_profile, driver2_profile)** – compares two drivers’ stats.
- **save_analysis_report(text, out_directory, filename)** – saves a markdown report to disk.
