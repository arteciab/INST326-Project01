import subprocess
import sys
import os

def run_test(name, command):
    print(f"\n=== Running {name} ===")
    try:
        result = subprocess.run(
            command, shell=True, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        print(result.stdout)
        print(f"{name} PASS")
        return True
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        print(f"{name} FAIL")
        return False


tests = [
    ("Project 3: Inheritance Test", "python tests/test_inheritance_local.py"),
    ("Project 3: Polymorphism Test", "python tests/polymorphism_test.py"),
    ("Project 3: Manager Composition Test", "python tests/manager_test.py"),
    ("Project 2: Datastore Test", "python tests/test_datastore.py"),
    ("Project 2: Driver Link Test", "python tests/test_driver_link.py"),
    ("Project 2: Racing Library Test", "python tests/test_racing_library.py"),
]

print("========================================")
print("     CHECKERED DATA FULL SYSTEM TEST     ")
print("========================================")

passed = 0
failed = 0

for name, cmd in tests:
    if run_test(name, cmd):
        passed += 1
    else:
        failed += 1

print("\n========================================")
print("               TEST SUMMARY")
print("========================================")
print(f"Total tests run: {len(tests)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print("========================================")

if failed == 0:
    print("\nAll tests PASSED. System is stable.\n")
else:
    print("\nSome tests FAILED. Review errors above.\n")
