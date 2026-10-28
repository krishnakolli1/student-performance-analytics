
from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_PATH = DATA_DIR / "student_performance.csv"


def main():
    """Generate realistic sample student performance data."""
    DATA_DIR.mkdir(exist_ok=True)

    rng = np.random.default_rng(42)
    student_count = 500

    data = pd.DataFrame({
        "Student_ID": [f"S{i:04d}" for i in range(1, student_count + 1)],
        "Gender": rng.choice(["Female", "Male"], student_count),
        "Study_Hours_Per_Week": rng.integers(1, 31, student_count),
        "Attendance_Percent": rng.integers(50, 101, student_count),
        "Previous_Score": rng.integers(35, 101, student_count),
        "Extracurricular_Activities": rng.choice(
            ["Yes", "No"], student_count, p=[0.45, 0.55]
        ),
    })

    # Generate scores influenced by study time, attendance,
    # and previous performance, with some random variation.
    noise = rng.normal(0, 8, student_count)
    base_score = (
        0.35 * data["Previous_Score"]
        + 0.8 * data["Study_Hours_Per_Week"]
        + 0.25 * data["Attendance_Percent"]
        + noise
    )

    data["Math_Score"] = np.clip(base_score + rng.normal(0, 7, student_count), 0, 100).round(1)
    data["Science_Score"] = np.clip(base_score + rng.normal(0, 8, student_count), 0, 100).round(1)
    data["English_Score"] = np.clip(base_score + rng.normal(0, 6, student_count), 0, 100).round(1)

    subject_columns = ["Math_Score", "Science_Score", "English_Score"]
    data["Average_Score"] = data[subject_columns].mean(axis=1).round(2)
    data["Performance_Level"] = pd.cut(
        data["Average_Score"],
        bins=[-1, 49, 69, 84, 100],
        labels=["Needs Improvement", "Average", "Good", "Excellent"]
    )

    data.to_csv(OUTPUT_PATH, index=False)

    print("Student dataset created successfully!")
    print(f"Students: {len(data)}")
    print(f"Columns: {len(data.columns)}")
    print(f"Saved to: {OUTPUT_PATH}")
    print("\nSample records:")
    print(data.head().to_string(index=False))


if __name__ == "__main__":
    main()
