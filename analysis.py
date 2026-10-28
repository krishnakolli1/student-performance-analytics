
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "student_performance.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    if not DATA_PATH.exists():
        print("Dataset not found. Run python create_dataset.py first.")
        return

    CHARTS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    # Clean and prepare data
    df = df.drop_duplicates(subset="Student_ID")
    df = df.dropna(
        subset=[
            "Math_Score",
            "Science_Score",
            "English_Score",
            "Attendance_Percent",
        ]
    )

    subjects = ["Math_Score", "Science_Score", "English_Score"]
    df["Average_Score"] = df[subjects].mean(axis=1)

    print("=" * 58)
    print("          STUDENT PERFORMANCE ANALYTICS")
    print("=" * 58)

    print(f"Students analyzed: {len(df)}")
    print(f"Average score: {df['Average_Score'].mean():.2f}")
    print(f"Average attendance: {df['Attendance_Percent'].mean():.2f}%")
    print(f"Average study hours/week: {df['Study_Hours_Per_Week'].mean():.2f}")
    print(f"Highest average score: {df['Average_Score'].max():.2f}")
    print(f"Lowest average score: {df['Average_Score'].min():.2f}")

    print("\nAverage score by subject:")
    print(df[subjects].mean().round(2).rename({
        "Math_Score": "Mathematics",
        "Science_Score": "Science",
        "English_Score": "English",
    }).to_string())

    print("\nPerformance level distribution:")
    print(df["Performance_Level"].value_counts().to_string())

    print("\nAverage score by attendance group:")
    df["Attendance_Group"] = pd.cut(
        df["Attendance_Percent"],
        bins=[0, 60, 75, 90, 100],
        labels=["0-60%", "61-75%", "76-90%", "91-100%"],
        include_lowest=True,
    )
    print(
        df.groupby("Attendance_Group", observed=False)["Average_Score"]
        .mean()
        .round(2)
        .to_string()
    )

    print("\nAverage score by study hours:")
    df["Study_Group"] = pd.cut(
        df["Study_Hours_Per_Week"],
        bins=[0, 5, 10, 20, 30],
        labels=["1-5 hours", "6-10 hours", "11-20 hours", "21-30 hours"],
        include_lowest=True,
    )
    print(
        df.groupby("Study_Group", observed=False)["Average_Score"]
        .mean()
        .round(2)
        .to_string()
    )

    # Chart 1: Average score by subject
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    subject_means = df[subjects].mean()
    sns.barplot(x=["Math", "Science", "English"], y=subject_means.values)
    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "average_score_by_subject.png", dpi=150)
    plt.close()

    # Chart 2: Score distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Average_Score"], bins=20, kde=True)
    plt.title("Distribution of Student Average Scores")
    plt.xlabel("Average Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "score_distribution.png", dpi=150)
    plt.close()

    # Chart 3: Attendance versus average score
    plt.figure(figsize=(8, 5))
    sns.regplot(
        data=df,
        x="Attendance_Percent",
        y="Average_Score",
        scatter_kws={"alpha": 0.45},
        line_kws={"color": "red"},
    )
    plt.title("Attendance vs. Average Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "attendance_vs_score.png", dpi=150)
    plt.close()

    # Chart 4: Study hours versus average score
    plt.figure(figsize=(8, 5))
    sns.regplot(
        data=df,
        x="Study_Hours_Per_Week",
        y="Average_Score",
        scatter_kws={"alpha": 0.45},
        line_kws={"color": "red"},
    )
    plt.title("Study Hours vs. Average Score")
    plt.xlabel("Study Hours per Week")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "study_hours_vs_score.png", dpi=150)
    plt.close()

    # Export reports
    df.to_csv(CHARTS_DIR / "cleaned_student_data.csv", index=False)

    subject_summary = pd.DataFrame({
        "Subject": ["Mathematics", "Science", "English"],
        "Average_Score": df[subjects].mean().values,
    })
    subject_summary.to_csv(
        CHARTS_DIR / "subject_summary.csv", index=False
    )

    performance_summary = (
        df["Performance_Level"]
        .value_counts()
        .rename_axis("Performance_Level")
        .reset_index(name="Student_Count")
    )
    performance_summary.to_csv(
        CHARTS_DIR / "performance_summary.csv", index=False
    )

    print(f"\nCharts and reports saved to: {CHARTS_DIR}")
    print("Analysis completed successfully!")


if __name__ == "__main__":
    main()

