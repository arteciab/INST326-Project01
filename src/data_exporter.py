import csv
import json
from pathlib import Path
import xml.etree.ElementTree as ET


class DataExporter:
    @staticmethod
    def export_races_csv(races, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        if not races:
            path.write_text("", encoding="utf-8")
            return 0

        fieldnames = list(races[0].keys())
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(races)
        return len(races)

    @staticmethod
    def export_results_csv(results, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        if not results:
            path.write_text("", encoding="utf-8")
            return 0

        fieldnames = list(results[0].keys())
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        return len(results)

    @staticmethod
    def export_drivers_json(drivers, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(drivers, indent=2), encoding="utf-8")
        return len(drivers)

    @staticmethod
    def export_races_json(races, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        payload = {"races": races}
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return len(races)

    @staticmethod
    def export_results_json(results, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        payload = {"results": results}
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return len(results)

    @staticmethod
    def export_races_xml(races, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        root = ET.Element("races")
        for r in races:
            race_el = ET.SubElement(root, "race")
            for k, v in r.items():
                child = ET.SubElement(race_el, str(k))
                child.text = str(v)

        ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)
        return len(races)

    @staticmethod
    def export_race_summary_report(race, results, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            "RACE SUMMARY REPORT",
            "",
            f"Race Summary: {race.get('name', '')}",
            f"Race ID: {race.get('race_id', '')}",
            f"Date: {race.get('date', '')}",
            f"Location: {race.get('location', '')}",
            "",
            "Results:",
        ]
        for r in results:
            lines.append(
                f"Driver {r.get('driver_id', '')} - Position {r.get('position', '')} - {r.get('points', '')} points"
            )

        path.write_text("\n".join(lines), encoding="utf-8")

    @staticmethod
    def export_driver_statistics_report(driver, driver_results, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        total_points = 0
        for r in driver_results:
            total_points += int(r.get("points", 0))

        lines = [
            f"Driver Stats: {driver.get('name', '')}",
            f"Driver ID: {driver.get('driver_id', '')}",
            f"Team: {driver.get('team', '')}",
            f"Total Results: {len(driver_results)}",
            f"Total Points: {total_points}",
        ]
        path.write_text("\n".join(lines), encoding="utf-8")

    @staticmethod
    def export_season_standings_report(drivers, results, file_path: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        points_by_driver = {}
        for r in results:
            did = r.get("driver_id")
            points_by_driver[did] = points_by_driver.get(did, 0) + int(r.get("points", 0))

        lines = ["Championship Standings:"]
        for d in drivers:
            did = d.get("driver_id")
            lines.append(f"{d.get('name', '')} ({did}) - {points_by_driver.get(did, 0)} pts")

        path.write_text("\n".join(lines), encoding="utf-8")

    @staticmethod
    def auto_export(data, file_path: str, data_type: str):
        ext = Path(file_path).suffix.lower()

        if ext == ".csv":
            if data_type == "races":
                return DataExporter.export_races_csv(data, file_path)
            if data_type == "results":
                return DataExporter.export_results_csv(data, file_path)
            raise ValueError("Unsupported CSV export type")

        if ext == ".json":
            if data_type == "races":
                return DataExporter.export_races_json(data, file_path)
            if data_type == "results":
                return DataExporter.export_results_json(data, file_path)
            if data_type == "drivers":
                return DataExporter.export_drivers_json(data, file_path)
            raise ValueError("Unsupported JSON export type")

        if ext == ".xml":
            if data_type == "races":
                return DataExporter.export_races_xml(data, file_path)
            raise ValueError("Unsupported XML export type")

        raise ValueError("Unsupported export format")
