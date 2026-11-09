
from pathlib import Path
from datetime import datetime
from collections import Counter
import csv
import json
import os
import time

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR
OUTPUT_DIR = BASE_DIR / "output"

CSV_FILE = DATA_DIR / "employees.csv"


def create_output_folder():
    OUTPUT_DIR.mkdir(exist_ok=True)


def check_csv_file():
    if not CSV_FILE.exists():
        print("Error: employees.csv was not found!")
        return False

    print("CSV absolute path:", CSV_FILE.resolve())
    return True




def backup_file(src, dst):
    line_count = 0

    with open(src, "r", encoding="utf-8") as source, \
         open(dst, "w", encoding="utf-8") as destination:

        for line in source:
            destination.write(line)
            line_count += 1

    return line_count




def log(message):
    log_path = OUTPUT_DIR / "log.txt"

    with open(log_path, "a", encoding="utf-8") as f:
        timestamp = datetime.now().isoformat()
        f.write(f"[{timestamp}] {message}\n")




def create_lock_file():
    lock_path = OUTPUT_DIR / "lock.txt"

    try:
        with open(lock_path, "x", encoding="utf-8") as f:
            f.write(datetime.now().isoformat())

        print("Lock file created.")

    except FileExistsError:
        print("ანგარიში უკვე შექმნილია")



def analyze_with_reader():

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as f:

        reader = csv.reader(f)

        header = next(reader)
        print("\nHEADER:")
        print(header)

        count = 0

        print("\nFIRST 3 EMPLOYEES:")

        for row in reader:
            if count < 3:
                print(row)

            count += 1

        print("\nTotal employees:", count)



def analyze_with_dictreader():

    department_counts = {}
    department_salaries = {}

    active_count = 0
    inactive_count = 0

    active_employees = []

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as f:

        reader = csv.DictReader(f)

        for employee in reader:

            department = employee["department"]
            salary = int(employee["salary"])

  

            department_counts[department] = (
                department_counts.get(department, 0) + 1
            )


            department_salaries[department] = (
                department_salaries.get(department, 0) + salary
            )

            # Active and inactive employees

            if employee["is_active"] == "True":

                active_count += 1
                active_employees.append(employee)

            else:
                inactive_count += 1



    department_stats = []

    for department in department_counts:

        count = department_counts[department]
        total_salary = department_salaries[department]

        average = round(total_salary / count, 2)

        department_stats.append({
            "department": department,
            "employee_count": count,
            "avg_salary": average
        })

    print("\nDEPARTMENT STATISTICS:")

    for stat in department_stats:
        print(stat)

    print("\nActive employees:", active_count)
    print("Inactive employees:", inactive_count)



    top_three = sorted(
        active_employees,
        key=lambda employee: int(employee["salary"]),
        reverse=True
    )[:3]

    print("\nTOP 3 ACTIVE EMPLOYEES:")

    for employee in top_three:

        print(
            employee["first_name"],
            employee["last_name"],
            employee["salary"]
        )

    return department_stats, active_employees

def save_department_stats(department_stats):

    department_stats.sort(
        key=lambda item: item["avg_salary"],
        reverse=True
    )

    output_path = OUTPUT_DIR / "department_stats.csv"

    fieldnames = [
        "department",
        "employee_count",
        "avg_salary"
    ]

    with open(output_path, "w", encoding="utf-8", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(department_stats)

    print("\nDepartment statistics saved.")


def save_high_earners(active_employees):

    output_path = OUTPUT_DIR / "high_earners.csv"

    rows = []

    for employee in active_employees:

        salary = int(employee["salary"])

        if salary >= 5000:

            full_name = (
                employee["first_name"] + " " +
                employee["last_name"]
            )

            rows.append([
                employee["id"],
                full_name,
                employee["department"],
                salary
            ])

    with open(output_path, "w", encoding="utf-8", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "id",
            "full_name",
            "department",
            "salary"
        ])

        writer.writerows(rows)

    print("High earners:", len(rows))



def safe_read(path):

    try:

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:

        log(f"File not found: {path}")
        print(f"File not found: {path}")

        return ""

    except UnicodeDecodeError:

        log(f"UnicodeDecodeError: {path}")
        print(f"Invalid UTF-8 encoding: {path}")

        with open(
            path,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as f:

            return f.read()


def create_broken_file():

    broken_path = OUTPUT_DIR / "broken.txt"

    with open(broken_path, "wb") as f:

        f.write(bytes([99, 97, 102, 233, 32, 255]))



def analyze_cities():

    cities = []

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as f:

        reader = csv.DictReader(f)

        for employee in reader:
            cities.append(employee["city"])

    city_counts = Counter(cities)

    top_three = city_counts.most_common(3)

    print("\nTOP 3 CITIES:")

    for city, count in top_three:
        print(city, count)

    output_path = OUTPUT_DIR / "cities.txt"

    with open(output_path, "w", encoding="utf-8") as f:

        print("TOP 3 CITIES:", file=f)

        for city, count in top_three:
            print(city, count, file=f)


def save_json_safe(data, path):

    temp_path = Path(str(path) + ".tmp")

    with open(temp_path, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    os.replace(temp_path, path)

    print("\nJSON saved successfully.")


class Timer:

    def __init__(self, name):

        self.name = name
        self.start_time = None

    def __enter__(self):

        print(f"\nSTART {self.name}")

        self.start_time = time.perf_counter()

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        elapsed = time.perf_counter() - self.start_time

        if exc_type is not None:

            print(
                f"FAILED {self.name}: "
                f"{exc_type.__name__} "
                f"({elapsed:.4f} seconds)"
            )

        else:

            print(
                f"FINISH {self.name}: "
                f"{elapsed:.4f} seconds"
            )

        return False


def main():


    create_output_folder()

    log("Program started")

    if not check_csv_file():
        log("Program stopped: CSV file missing")
        return

    create_lock_file()

    backup_path = OUTPUT_DIR / "employees_backup.csv"

    lines = backup_file(CSV_FILE, backup_path)

    print("\nBackup lines:", lines)

    log("Part 1 completed")



    with Timer("CSV ანალიზი"):

        analyze_with_reader()

        department_stats, active_employees = (
            analyze_with_dictreader()
        )

        save_department_stats(department_stats)

        save_high_earners(active_employees)

    log("Part 2 completed")



    missing_path = OUTPUT_DIR / "missing.txt"

    safe_read(missing_path)

    create_broken_file()

    broken_path = OUTPUT_DIR / "broken.txt"

    broken_content = safe_read(broken_path)

    print("\nBroken file content:", broken_content)

    analyze_cities()

    summary_path = OUTPUT_DIR / "summary.json"

    save_json_safe(department_stats, summary_path)

    log("Part 3 completed")



    try:

        with Timer("test"):
            1 / 0

    except ZeroDivisionError:

        print("ZeroDivisionError caught outside Timer")

    log("Part 4 completed")


    log("Program finished")

    print("\nHR Report completed successfully!")


if __name__ == "__main__":
    main()
