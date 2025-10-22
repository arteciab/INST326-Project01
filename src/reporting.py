# src/reporting.py
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Optional


def format_race_summary(
    race: Dict[str, Any],
    results: List[Dict[str, Any]],
    drivers_by_id: Dict[str, Dict[str, Any]],
    top_n: int = 10,
) -> str:
    """
    Build a simple text summary for a race.

    Expected keys:
      race: {"race_id": str, "name": str, "date": "YYYY-MM-DD" or date}
      results: each item has {"race_id": str, "driver_id": str, "pos": int|None, "best_lap": str|None}
      drivers_by_id: driver_id -> {"name": str, "team": str}

    Returns:
      Markdown-friendly multi-line string.
    """
    race_id = race.get("race_id")
    race_name = race.get("name", "Unknown Race")
    race_date = race.get("date", "Unknown Date")

    # Filter results for this race
    race_results = [r for r in results if r.get("race_id") == race_id]

    header = f"# {race_name} ({race_date})"
    if not race_results:
        return header + "\nNo results available."

    # Sort: DNFs (pos=None) at the end; otherwise by position ascending
    def sort_key(r: Dict[str, Any]) -> tuple[bool, int]:
        pos = r.get("pos")
        is_dnf = pos is None
        pos_val = int(pos) if isinstance(pos, int) else 10**9
        return (is_dnf, pos_val)

    race_results.sort(key=sort_key)

    lines: List[str] = [header]
    for r in race_results[:top_n]:
        driver = drivers_by_id.get(r.get("driver_id", ""), {})
        driver_name = driver.get("name", "Unknown Driver")
        team_name = driver.get("team", "Unknown Team")
        pos = r.get("pos")
        finishing_tag = f"P{pos}" if isinstance(pos, int) else "DNF"
        best_lap_display = r.get("best_lap")
        best_lap_display = best_lap_display if best_lap_display not in (None, "") else "N/A"
        lines.append(f"{finishing_tag} - {driver_name} ({team_name}) - Best Lap: {best_lap_display}")

    return "\n".join(lines)


def generate_driver_profile(
    driver_id: str,
    all_results: List[Dict[str, Any]],
    drivers_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Compute a simple driver profile summary.

    Returns a dict:
      {
        "name": str,
        "starts": int,
        "finishes": List[int | 'DNF'],
        "podiums": int,
        "best_finish": Optional[int]
      }
    """
    driver = drivers_by_id.get(driver_id, {})
    driver_name = driver.get("name", "Unknown Driver")

    driver_results = [r for r in all_results if r.get("driver_id") == driver_id]
    starts = len(driver_results)

    finishes_with_dnfs: List[Any] = [
        (res.get("pos") if isinstance(res.get("pos"), int) else "DNF")
        for res in driver_results
    ]
    numeric_finishes = [res.get("pos") for res in driver_results if isinstance(res.get("pos"), int)]
    podiums = sum(1 for pos in numeric_finishes if pos <= 3)
    best_finish: Optional[int] = min(numeric_finishes) if numeric_finishes else None

    return {
        "name": driver_name,
        "starts": starts,
        "finishes": finishes_with_dnfs,
        "podiums": podiums,
        "best_finish": best_finish,
    }


def format_comparison_output(driver1_profile: Dict[str, Any], driver2_profile: Dict[str, Any]) -> str:
    """
    Turn two driver profile dicts into a readable side-by-side comparison.
    """
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

    def show_best(x: Any) -> str:
        return str(x) if isinstance(x, int) else "–"

    def join_finishes(seq: List[Any]) -> str:
        def show_one(v: Any) -> str:
            return f"P{v}" if isinstance(v, int) else "DNF"
        return ", ".join(show_one(v) for v in seq) if seq else "None"

    lines = [
        f"{d1_name} vs {d2_name}",
        f"Starts: {d1_starts} vs {d2_starts}",
        f"Finishes: {join_finishes(d1_finishes)} vs {join_finishes(d2_finishes)}",
        f"Podiums: {d1_podiums} vs {d2_podiums}",
        f"Best Finish: {show_best(d1_best)} vs {show_best(d2_best)}",
    ]
    return "\n".join(lines)


def save_analysis_report(text: str, out_directory: str, filename: str = "report.md", overwrite: bool = False) -> str:
    """
    Write 'text' into out_directory/filename. Creates the folder if missing.

    Raises:
        FileExistsError if file exists and overwrite=False.
    """
    out_path = Path(out_directory)
    out_path.mkdir(parents=True, exist_ok=True)

    target = out_path / filename
    if target.exists() and not overwrite:
        raise FileExistsError(f"File {target} already exists and overwrite is False.")

    target.write_text(text, encoding="utf-8")
    return str(target)
