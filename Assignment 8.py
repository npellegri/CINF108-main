from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Dict, Tuple, Any, Optional

# ----- 1. Copy a text file -----
def copy_text_file(src: str | Path, dst: str | Path) -> None:
    """Copy the contents of a text file `src` into `dst`."""
    src = Path(src)
    dst = Path(dst)
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


# ----- 2. Highest scoring student from CSV (name, score) -----
def highest_scoring_student(csv_path: str | Path) -> Tuple[str, float]:
    """Return (name, score) of the student with the highest score."""
    top_name = ""
    top_score = float("-inf")
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "name" not in reader.fieldnames or "score" not in reader.fieldnames:
            raise ValueError("CSV must have columns: name, score")
        for row in reader:
            try:
                score = float(row["score"])
            except (TypeError, ValueError):
                continue
            if score > top_score:
                top_score = score
                top_name = row["name"]
    if top_name == "":
        raise ValueError("No valid rows found.")
    return top_name, top_score


# ----- 3. Count words and lines in a text file -----
def count_words_lines(path: str | Path) -> Tuple[int, int]:
    """Return (num_lines, num_words) for a text file."""
    text = Path(path).read_text(encoding="utf-8")
    num_lines = text.count("\\n") + (0 if text == "" else 1)
    # Split on any whitespace
    words = text.split()
    return num_lines, len(words)


# ----- 4. Write a list of sentences to a new text file, one per line -----
def write_sentences(sentences: Iterable[str], out_path: str | Path) -> None:
    """Write each sentence on its own line."""
    with open(out_path, "w", encoding="utf-8") as f:
        for s in sentences:
            f.write(str(s).rstrip("\\n") + "\\n")


# ----- 5. Average salary from employee CSV (name, age, salary) -----
def average_salary(csv_path: str | Path) -> float:
    """Compute average salary across all rows with numeric salary."""
    total = 0.0
    count = 0
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        needed = {"name", "age", "salary"}
        if not needed.issubset(set(reader.fieldnames or [])):
            raise ValueError("CSV must have columns: name, age, salary")
        for row in reader:
            try:
                total += float(row["salary"])
                count += 1
            except (TypeError, ValueError):
                continue
    if count == 0:
        raise ValueError("No valid salary rows.")
    return total / count


# ----- 6. Total sales revenue for a specific product from CSV -----
def total_revenue_for_product(csv_path: str | Path, product_name: str) -> float:
    """
    Find total sales revenue for `product_name`.
    Accepts either columns:
      - product, units_sold, unit_price    (revenue = units_sold * unit_price)
      - product, revenue                   (revenue given directly)
    Case-insensitive match on product name.
    """
    product_name_lc = product_name.strip().lower()
    total = 0.0
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = set(reader.fieldnames or [])
        uses_multiplicative = {"product", "units_sold", "unit_price"}.issubset(fields)
        uses_revenue = {"product", "revenue"}.issubset(fields)
        if not (uses_multiplicative or uses_revenue):
            raise ValueError("CSV must have columns for either (product, units_sold, unit_price) or (product, revenue).")
        for row in reader:
            if str(row.get("product", "")).strip().lower() != product_name_lc:
                continue
            if uses_multiplicative:
                try:
                    total += float(row["units_sold"]) * float(row["unit_price"])
                except (TypeError, ValueError):
                    continue
            else:
                try:
                    total += float(row["revenue"])
                except (TypeError, ValueError):
                    continue
    return total


# ----- 7. Sum all numbers in a text file -----
def sum_numbers_in_file(path: str | Path) -> float:
    """
    Read a text file containing numbers (one per line or whitespace-separated)
    and return the sum.
    """
    text = Path(path).read_text(encoding="utf-8")
    total = 0.0
    for token in text.split():
        try:
            total += float(token)
        except ValueError:
            # Ignore non-numeric tokens
            pass
    return total


# ----- 8. Bar chart from CSV using Matplotlib -----
def bar_chart_from_csv(csv_path: str | Path, x_col: str, y_col: str, out_png: str | Path) -> None:
    """
    Read a CSV and render a bar chart of y_col vs x_col using matplotlib.
    The image is saved to `out_png`.
    """
    import matplotlib.pyplot as plt

    xs: List[Any] = []
    ys: List[float] = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if x_col in row and y_col in row:
                xs.append(row[x_col])
                try:
                    ys.append(float(row[y_col]))
                except (TypeError, ValueError):
                    ys.append(0.0)

    # Plot: one chart, no specific colors/styles set
    plt.figure()
    plt.bar(xs, ys)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} by {x_col}")
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()


# ----- 9. Read JSON and extract specific information -----
def read_json_extract(json_path: str | Path, keys: Iterable[str]) -> Dict[str, Any]:
    """
    Extract selected keys from a JSON file. Supports dot notation for nested keys.
    Example key: "user.name" looks up obj['user']['name'] if present.
    """
    def get_nested(d: Any, dotted: str) -> Any:
        cur: Any = d
        for part in dotted.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return None
        return cur

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {k: get_nested(data, k) for k in keys}


# ----- 10. Average temperature for each day from CSV -----
def average_temp_by_day(csv_path: str | Path) -> Dict[str, float]:
    """
    Given CSV with columns like: day, temperature
    Return mapping of day -> average temperature.
    """
    sums: Dict[str, float] = {}
    counts: Dict[str, int] = {}

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "day" not in reader.fieldnames or "temperature" not in reader.fieldnames:
            raise ValueError("CSV must have columns: day, temperature")
        for row in reader:
            day = row["day"]
            try:
                temp = float(row["temperature"])
            except (TypeError, ValueError):
                continue
            sums[day] = sums.get(day, 0.0) + temp
            counts[day] = counts.get(day, 0) + 1

    return {day: (sums[day] / counts[day]) for day in sums}


# ----- Demo utilities -----
def _make_sample_files(base: Path) -> dict:
    """Create small sample files used in main(); return their paths."""
    base.mkdir(parents=True, exist_ok=True)

    # Text file for 1 & 3
    text1 = base / "sample.txt"
    text1.write_text("hello world\\nthis is a test file\\nwith three lines", encoding="utf-8")
    text2 = base / "copy_of_sample.txt"  # destination for 1

    # Sentences for 4
    sentences_out = base / "sentences.txt"

    # Students CSV for 2
    students_csv = base / "students.csv"
    with open(students_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows([
            {"name": "Ava", "score": 87},
            {"name": "Ben", "score": 93},
            {"name": "Cara", "score": 91},
        ])

    # Employees CSV for 5
    employees_csv = base / "employees.csv"
    with open(employees_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "salary"])
        writer.writeheader()
        writer.writerows([
            {"name": "Dee", "age": 29, "salary": 65000},
            {"name": "Eli", "age": 41, "salary": 72000},
            {"name": "Flo", "age": 35, "salary": 70000},
        ])

    # Sales CSV for 6
    sales_csv = base / "sales.csv"
    with open(sales_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["product", "units_sold", "unit_price"])
        writer.writeheader()
        writer.writerows([
            {"product": "Widget", "units_sold": 10, "unit_price": 3.5},
            {"product": "Gadget", "units_sold": 5, "unit_price": 8.0},
            {"product": "Widget", "units_sold": 7, "unit_price": 3.5},
        ])

    # Numbers text for 7
    nums_txt = base / "numbers.txt"
    nums_txt.write_text("1\\n2 3\\n4\\n5.5", encoding="utf-8")

    # CSV for bar chart 8
    bars_csv = base / "bars.csv"
    with open(bars_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "value"])
        writer.writeheader()
        writer.writerows([
            {"category": "A", "value": 10},
            {"category": "B", "value": 7},
            {"category": "C", "value": 12},
        ])
    bar_png = base / "bar_chart.png"

    # JSON for 9
    sample_json = base / "data.json"
    with open(sample_json, "w", encoding="utf-8") as f:
        json.dump({"user": {"name": "Nick", "role": "Student"}, "course": "COM100", "year": 2025}, f, indent=2)

    # Temps CSV for 10
    temps_csv = base / "temps.csv"
    with open(temps_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["day", "temperature"])
        writer.writeheader()
        rows = [
            ("Mon", 60), ("Mon", 62), ("Tue", 58),
            ("Tue", 61), ("Wed", 65), ("Wed", 64),
        ]
        for d, t in rows:
            writer.writerow({"day": d, "temperature": t})

    return {
        "text1": text1,
        "text2": text2,
        "sentences_out": sentences_out,
        "students_csv": students_csv,
        "employees_csv": employees_csv,
        "sales_csv": sales_csv,
        "nums_txt": nums_txt,
        "bars_csv": bars_csv,
        "bar_png": bar_png,
        "sample_json": sample_json,
        "temps_csv": temps_csv,
    }


def main() -> None:
    base = Path(__file__).with_suffix("").parent / "sample_io"
    base.mkdir(exist_ok=True, parents=True)
    paths = _make_sample_files(base)

    # 1
    copy_text_file(paths["text1"], paths["text2"])

    # 2
    top_student = highest_scoring_student(paths["students_csv"])

    # 3
    lines, words = count_words_lines(paths["text1"])

    # 4
    write_sentences(["Line one.", "Line two.", "Line three."], paths["sentences_out"])

    # 5
    avg_sal = average_salary(paths["employees_csv"])

    # 6
    widget_rev = total_revenue_for_product(paths["sales_csv"], "Widget")

    # 7
    total_sum = sum_numbers_in_file(paths["nums_txt"])

    # 8
    bar_chart_from_csv(paths["bars_csv"], "category", "value", paths["bar_png"])

    # 9
    extracted = read_json_extract(paths["sample_json"], ["user.name", "user.role", "course", "year", "missing.key"])

    # 10
    avg_temps = average_temp_by_day(paths["temps_csv"])

    # Print demo results
    print("1) Copied sample.txt -> copy_of_sample.txt")
    print(f"2) Highest score: {top_student[0]} with {top_student[1]}")
    print(f"3) Lines: {lines}, Words: {words}")
    print(f"4) Wrote sentences to: {paths['sentences_out'].name}")
    print(f"5) Average salary: {avg_sal:.2f}")
    print(f"6) Total revenue for Widget: {widget_rev:.2f}")
    print(f"7) Sum of numbers: {total_sum}")
    print(f"8) Bar chart saved to: {paths['bar_png'].name}")
    print(f"9) Extracted JSON keys: {extracted}")
    print(f"10) Average temperatures: {avg_temps}")


if __name__ == "__main__":
    main()
