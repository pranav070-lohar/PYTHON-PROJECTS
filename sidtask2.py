import csv
from fpdf import FPDF
import os
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create sample CSV file
csv_filename = "student_scores.csv"
data = [
    ["Name", "Math", "Science", "English"],
    ["Alice", 85, 90, 88],
    ["Bob", 78, 82, 80],
    ["Charlie", 92, 88, 91],
    ["David", 70, 75, 72],
    ["Eva", 88, 85, 90]
]

with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Step 2: Read CSV and analyze
students = []
subjects = data[0][1:]
averages = {subject: 0 for subject in subjects}
top_scorer = ("", 0)

for row in data[1:]:
    name = row[0]
    scores = list(map(int, row[1:]))
    total = sum(scores)
    students.append((name, scores, total))

    # Add to average
    for i, score in enumerate(scores):
        averages[subjects[i]] += score

    # Check top scorer
    if total > top_scorer[1]:
        top_scorer = (name, total)

# Compute average
num_students = len(students)
for subject in subjects:
    averages[subject] = round(averages[subject] / num_students, 2)

# Step 3: Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Student Performance Report", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(200, 10, "Average Scores:", ln=True)

for subject in subjects:
    pdf.cell(200, 10, f"{subject}: {averages[subject]}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, f"Top Scorer: {top_scorer[0]} with total {top_scorer[1]}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, "Detailed Scores:", ln=True)

# Table header
pdf.set_font("Arial", 'B', 12)
pdf.cell(40, 10, "Name")
for subject in subjects:
    pdf.cell(30, 10, subject)
pdf.cell(30, 10, "Total")
pdf.ln()

# Table data
pdf.set_font("Arial", '', 12)
for student in students:
    name, scores, total = student
    pdf.cell(40, 10, name)
    for score in scores:
        pdf.cell(30, 10, str(score))
    pdf.cell(30, 10, str(total))
    pdf.ln()

# Save PDF before adding the chart
pdf.output("student_report.pdf")
print("PDF report generated as 'student_report.pdf'")

# Step 4: Create a bar chart for average scores
plt.figure(figsize=(8, 5))
subjects = list(averages.keys())
avg_scores = list(averages.values())
plt.bar(subjects, avg_scores, color='skyblue')
plt.title('Average Scores by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.xticks(rotation=45)

# Save the chart as an image
plt.savefig("average_scores_chart.png")

# Add the chart to the PDF
pdf = FPDF()
pdf.add_page()
pdf.image("average_scores_chart.png", x=10, y=30, w=190)  # Adjust position and size as needed
pdf.output("student_report_with_chart.pdf")
print("Updated PDF report generated as 'student_report_with_chart.pdf'")
