# 1)
def format_race_summary(race: Race, results: List[Result], drivers_by_id: Dict[str, Driver], top_n: int = 10) -> str:
    race_results = []
    for result in results:
        if result.race_id == Race.race_id:
            race_results.append(result)
    header = f"# {race.name} ({race.date})"
    if not race_results:
        return header + "\nNo results available."
    # Sort results by position, with none being at the end for DNFS
    def make_sort_key(result: Result):
        is_dnf = (race_result.pos is None)
        position_or_dnf = race_result.pos if race_result.pos is not None else int(1000)
        return (is_dnf, position_or_dnf)
    race_results.sort(key=make_sort_key)
    lines = []
    for race_result in race_results[:top_n]:
        driver = drivers_by_id.get(race_result.driver_id)
        driver_name = driver.name if driver else "Unknown Driver"
        team_name = driver.team if driver else "Unknown Team"
        finishing_tag = f"P{race_result.pos}" if race_result.pos is not None else "DNF"
        best_lap_display = race_result.best_lap if race_result.best_lap is not None else "N/A"
        lines.append(f"{finishing_tag} - {driver_name} ({team_name}) - Best Lap: {best_lap_display}")

    return "\n".join(lines)

# 2)
def generate_driver_profile(driver_id: str, all_results: List[Result]) -> str:
    """Returns the name, finishes, starts, podiums and best finish for a driver given their ID."""
    driver = drivers_by_id.get(driver_id)
    driver_name = driver.name if driver else "Unknown Driver"
    driver_results = [result for result in all_results if result.driver_id == driver_id]
    starts = len(driver_results)
    finishes_with_dnfs = [
        (res.pos if isinstance(res.pos, int) else "DNF")
        for res in driver_results
    ]
    numeric_finishes = [res.pos for res in driver_results if isinstance(res.pos, int)] 
    podiums = sum(1 for pos in numeric_finishes if pos <= 3)
    best_finish = min(numeric_finishes) if numeric_finishes else None
    return {
        "name": driver_name,
        "starts": starts,
        "finishes": finishes_with_dnfs,
        "podiums": podiums,
        "best_finish": best_finish
    }

#3) 
def format_comparison_output(driver1_profile: dict, driver2_profile: dict) -> str:
    """Formats a comparison between two drivers, returning a string."""
    d1_name = driver1_profile.get("name", "Driver 1")
    d2_name = driver2_profile.get("name", "Driver 2")

    d1_starts = driver1_profile.get("starts", 0)
    d2_starts = driver2_profile.get("starts", 0)

    d1_finishes = driver1_profile.get("finishes", [])
    d2_finishes = driver2_profile.get("finishes", [])

    d1_podiums = driver1_profile.get("podiums", 0)
    d2_podiums = driver2_profile.get("podiums", 0)

    d1_best = driver1_profile.get("best_finish")
    d2_best = driver2_profile.get("best_finish")

    def show_best(x): 
        return x if isinstance(x, int) else "–"
    def join_finishes(seq):
        # Turn [1, "DNF", 4] into "P1, DNF, P4"
        def show_one(v):
            return f"P{v}" if isinstance(v, int) else "DNF"
        return ", ".join(show_one(v) for v in seq) if seq else "None"
    lines = [
        f"{d1_name} vs {d2_name}",
        f"Starts: {d1_starts} vs {d2_starts}",
        f"Finishes: {join_finishes(d1_finishes)} vs {join_finishes(d2_finishes)}",
        f"Podiums: {d1_podiums} vs {d2_podiums}",
        f"Best Finish: {show_best(d1_best)} vs {show_best(d2_best)}"
    ]
    return "\n".join(lines)

# 4)
def save_analysis_report(text: str, out_directory: str, filename: str = "report.md", overwrite: bool = False) -> str:

    """Writes 'text' to out_directory/filename, creates a folder if it doesn't exist.
    Throws an error if the file exists and overwrite is False. returns path as a string"""
    out_path = Path(out_directory)
    out_path.mkdir(parents=True, exist_ok=True)

    target = out_path / filename
    if target.exists() and not overwrite:
        raise FileExistsError(f"File {target} already exists and overwrite is False.")
    
    target.write_text(text, encoding="utf-8")
    return str(target)

# 5) import pandas as pd
from pandas.api.types import is_integer_dtype, is_float_dtype, is_string_dtype

def validate_data_sources_min(
    dataframes_by_name: dict[str, pd.DataFrame],
    validation_rules: dict
) -> dict:
    """
    Validate tables (schema/types/PK/refs). Returns {'passed': bool, 'errors': [...]}.
    """
    errors: list[str] = []

    # Per-table: required columns, coarse dtypes, primary key duplicates
    for table_name, table_rules in validation_rules.get("tables", {}).items():
        if table_name not in dataframes_by_name:
            errors.append(f"[{table_name}] missing DataFrame")
            continue

        table_df = dataframes_by_name[table_name]

        for required_col in table_rules.get("required", []):
            if required_col not in table_df.columns:
                errors.append(f"[{table_name}] missing column '{required_col}'")

        # Expected types (int / float / string / date)
        for col_name, expected_type in table_rules.get("types", {}).items():
            if col_name not in table_df.columns:
                continue
            col = table_df[col_name]
            is_ok = (
                (expected_type == "int"    and is_integer_dtype(col)) or
                (expected_type == "float"  and (is_float_dtype(col) or is_integer_dtype(col))) or
                (expected_type == "string" and is_string_dtype(col)) or
                (expected_type == "date"   and pd.to_datetime(col, errors="coerce").notna().all())
            )
            if not is_ok:
                errors.append(f"[{table_name}] '{col_name}' type != {expected_type}")

        # Primary key uniqueness
        primary_key = table_rules.get("pk", [])
        if primary_key and set(primary_key).issubset(table_df.columns):
            duplicate_count = table_df.duplicated(subset=primary_key).sum()
            if duplicate_count:
                errors.append(f"[{table_name}] {duplicate_count} duplicate PK rows {primary_key}")

    # Referential integrity: child column values must exist in parent column
    for relation in validation_rules.get("refs", []):
        child_table_name       = relation["child"]
        child_key_column       = relation["child_key"]
        parent_table_name      = relation["parent"]
        parent_key_column      = relation["parent_key"]

        if child_table_name in dataframes_by_name and parent_table_name in dataframes_by_name:
            child_values  = set(dataframes_by_name[child_table_name][child_key_column].dropna())
            parent_values = set(dataframes_by_name[parent_table_name][parent_key_column].dropna())
            missing_values = child_values - parent_values
            if missing_values:
                errors.append(
                    f"[ref] {child_table_name}.{child_key_column} has {len(missing_values)} "
                    f"value(s) not found in {parent_table_name}.{parent_key_column}"
                )

    return {"passed": not errors, "errors": errors}

