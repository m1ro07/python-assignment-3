import csv
import json
import os


input_file = "/Users/market/Downloads/global_university_students_performance_habits_10000.csv"
output_folder = "/Users/market/Documents/New project/output"
output_file = "/Users/market/Documents/New project/output/result.json"


if not os.path.exists(input_file):
    print("File not found:", input_file)
else:
    os.makedirs(output_folder, exist_ok=True)


students = []
with open(input_file, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    test = list(reader)

    students = sorted(test, key=lambda x: float(x['final_exam_score']), reverse=True)

top_10_students = []

for i, student in enumerate(students[:10], start=1):
    top_10_students.append(
                {
                    "rank": i,
                    "student_id": student["student_id"],
                    "country": student["country"],
                    "major": student["major"],
                    "GPA": student["GPA"],
                    "final_exam_score": student["final_exam_score"],
                }
            )
result = {
                "variant": "D",
                "analysis_task": "Top 10 Students",
                "ranking_basis": "final_exam_score",
                "students_processed": len(students),
                "top_10_students": top_10_students,
            }


with open(output_file, "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)

print("Practice 4 - Variant D")
print("Dataset:", os.path.basename(input_file))
for i, student in enumerate(students):
    if i == 5:
        break
    print(
            student["student_id"],
            student["age"],
            student["gender"],
            student["country"],
            student["GPA"]
        )
    print("Total students:", len(students))
    print("Top 10 Students by Final Exam Score:")

for student in top_10_students:
    print(
            student['rank'],
            student['student_id'],
            student['country'],
            student['major'],
            student['GPA'],
            student['final_exam_score'],
            f'{student["rank"]}. '
            f'ID: {student["student_id"]}, '
            f'Country: {student["country"]}, '
            f'Major: {student["major"]}, '
            f'GPA: {student["GPA"]}, '
            f'Final Exam Score: {student["final_exam_score"]}'
        )

print("JSON file saved to:", output_file)