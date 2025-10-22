import csv
from datetime import datetime
# Calculates the average finish time from a list of finish times.
def calculate_average_finish(filename):
    finish_times = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    time = float(line.strip())
                    finish_times.append(time)
                except ValueError:
                    # Skip lines that don't contain valid numbers
                    continue
        
        if not finish_times:
            return None
        
        return sum(finish_times) / len(finish_times)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


# Validates driver data from a CSV file and returns a list of valid entries.
def validate_driver_data(filename):
    valid_data = []
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                name = row.get('Driver Name', '').strip()
                time_str = row.get('Finish Time', '').strip()
                
                # Check name validity
                if not name:
                    print(f" Skipping entry with missing driver name: {row}")
                    continue
                
                # Check time validity
                try:
                    time = float(time_str)
                    if time < 0:
                        print(f" Invalid (negative) finish time for {name}: {time}")
                        continue
                except ValueError:
                    print(f" Invalid or missing finish time for {name}: '{time_str}'")
                    continue
                
                valid_data.append((name, time))
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return valid_data

# Searches for a specific driver's finish time in a CSV file.
def search_driver_results(filename, driver_name):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                name = row.get('Driver Name', '').strip()
                time_str = row.get('Finish Time', '').strip()
                # Case-insensitive match
                if name.lower() == driver_name.lower():  
                    try:
                        time = float(time_str)
                        return time
                    except ValueError:
                        print(f"Invalid finish time for {name}: '{time_str}'")
                        return None
                    
        print(f"Driver '{driver_name}' not found in file.")
        return None
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


#  Filters a the data by a specific team name from a CSV file.
def filter_by_team(filename, team_name):
    filtered_results = []
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                team = row.get('Team', '').strip()
                # Case-insensitive match
                if team.lower() == team_name.lower():  
                    filtered_results.append({
                        'Driver Name': row.get('Driver Name', '').strip(),
                        'Team': team,
                        'Finish Time': row.get('Finish Time', '').strip()
                    })
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    
    if not filtered_results:
        print(f"No results found for team '{team_name}'.")
    
    return filtered_results

# sorts the races by date from a CSV file.
def sort_races_by_date(filename, descending=False):
    race_data = []
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                date_str = row.get('Race Date', '').strip()
                try:
                    race_date = datetime.strptime(date_str, "%Y-%m-%d")
                    row['Race Date'] = race_date  # store as datetime for easy sorting
                    race_data.append(row)
                except ValueError:
                    print(f"Invalid or missing date format: '{date_str}' (expected YYYY-MM-DD)")
                    continue
        
        # Sort by date
        race_data.sort(key=lambda x: x['Race Date'], reverse=descending)
        
        # Convert back to strings for readability
        for row in race_data:
            row['Race Date'] = row['Race Date'].strftime("%Y-%m-%d")
        
        return race_data
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


