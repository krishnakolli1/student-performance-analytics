# Student Performance Analytics

## Project Overview
This project analyzes sample academic data for 500 students to explore subject scores, attendance, study habits, and overall academic performance.

The project uses Python to clean and analyze student data, identify patterns, generate visualizations, and export summary reports.

**Note:** The dataset is synthetic and was generated for educational and portfolio demonstration purposes. It does not represent real students.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Analysis Performed
- Calculated average student scores across Mathematics, Science, and English.
- Compared average scores between subjects.
- Examined the distribution of student performance levels.
- Explored the relationship between attendance and academic scores.
- Explored the relationship between weekly study hours and academic scores.
- Exported cleaned data and summary reports to CSV files.

## Visualizations
The analysis generates four charts:

1. `average_score_by_subject.png` — compares average scores by subject.
2. `score_distribution.png` — displays the distribution of average student scores.
3. `attendance_vs_score.png` — explores attendance and academic performance.
4. `study_hours_vs_score.png` — explores study time and academic performance.

## Project Structure
```text
student-performance-analytics/
├── data/
│   └── student_performance.csv
├── charts/
│   ├── average_score_by_subject.png
│   ├── score_distribution.png
│   ├── attendance_vs_score.png
│   ├── study_hours_vs_score.png
│   ├── cleaned_student_data.csv
│   ├── subject_summary.csv
│   └── performance_summary.csv
├── create_dataset.py
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate the sample dataset:
   ```bash
   python create_dataset.py
   ```
4. Run the analysis:
   ```bash
   python analysis.py
   ```

Charts and reports will be saved in the `charts/` directory.

## Skills Demonstrated
- Data generation and preprocessing
- Exploratory data analysis (EDA)
- Descriptive statistics
- Grouping and comparing student performance
- Data visualization
- CSV report generation

## Disclaimer
This project uses synthetic data for educational purposes only. Observed patterns are illustrative and should not be interpreted as evidence of real-world causal relationships.
