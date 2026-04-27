import csv
import json
import os


INPUT_FILE = "/Users/market/Downloads/global_university_students_performance_habits_10000.csv"
OUTPUT_FOLDER = "/Users/market/Documents/New project/output"
OUTPUT_FILE = "/Users/market/Documents/New project/output/result.json"


def load_students(file_path):
    students = []

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "student_id": row["student_id"],
                "age": row["age"],
                "gender": row["gender"],
                "country": row["country"],
                "major": row["major"],
                "GPA": float(row["GPA"]),
                "final_exam_score": float(row["final_exam_score"]),
            }
            students.append(student)

    return students


def get_top_students(students, n=10):
    sorted_students = sorted(
        students,
        key=lambda student: student["final_exam_score"],
        reverse=True,
    )

    top_students = []

    for i, student in enumerate(sorted_students[:n], start=1):
        top_students.append(
            {
                "rank": i,
                "student_id": student["student_id"],
                "country": student["country"],
                "major": student["major"],
                "GPA": student["GPA"],
                "final_exam_score": student["final_exam_score"],
            }
        )

    return top_students


def save_result(result, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)


def main():
    try:
        if not os.path.exists(INPUT_FILE):
            raise FileNotFoundError(f"File not found: {INPUT_FILE}")

        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        students = load_students(INPUT_FILE)
        top_10_students = get_top_students(students, 10)

        result = {
            "variant": "D",
            "analysis_task": "Top 10 Students",
            "ranking_basis": "final_exam_score",
            "students_processed": len(students),
            "top_10_students": top_10_students,
        }

        save_result(result, OUTPUT_FILE)

        print("Practice 5 - Variant D")
        print("Function: get_top_students(students, n=10)")
        print("Dataset:", os.path.basename(INPUT_FILE))
        print("First 5 students:")

        for student in students[:5]:
            print(
                student["student_id"],
                student["age"],
                student["gender"],
                student["country"],
                student["GPA"],
            )


        print("Total students:", len(students))
        print("Top 10 Students by Final Exam Score:")

        for student in top_10_students:
            print(
                f'{student["rank"]}. '
                f'ID: {student["student_id"]}, '
                f'Country: {student["country"]}, '
                f'Major: {student["major"]}, '
                f'GPA: {student["GPA"]}, '
                f'Final Exam Score: {student["final_exam_score"]}'
            )

        print("JSON file saved to:", OUTPUT_FILE)

    except FileNotFoundError as error:
        print(error)
    except ValueError as error:
        print("Data conversion error:", error)
    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()