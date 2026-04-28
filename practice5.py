import csv
import json
import os


DEFAULT_INPUT_FILE = "students.csv"
FALLBACK_INPUT_FILE = "/Users/market/Downloads/global_university_students_performance_habits_10000.csv"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "practice5_result.json")


def get_input_file():
    if os.path.exists(DEFAULT_INPUT_FILE):
        return DEFAULT_INPUT_FILE

    if os.path.exists(FALLBACK_INPUT_FILE):
        return FALLBACK_INPUT_FILE

    raise FileNotFoundError("CSV file not found.")


def load_students(input_file):
    students = []

    with open(input_file, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(
                {
                    "student_id": row["student_id"],
                    "age": int(row["age"]),
                    "gender": row["gender"],
                    "country": row["country"],
                    "major": row["major"],
                    "GPA": float(row["GPA"]),
                    "final_exam_score": float(row["final_exam_score"]),
                }
            )

    return students


def valid_student(student):
    return student["final_exam_score"] >= 0


def score_key(student):
    return student["final_exam_score"]


def add_rank(item):
    rank = item[0]
    student = item[1]

    return {
        "rank": rank,
        "student_id": student["student_id"],
        "country": student["country"],
        "major": student["major"],
        "GPA": student["GPA"],
        "final_exam_score": student["final_exam_score"],
    }


def get_top_students(students, n=10):
    valid_students = list(filter(valid_student, students))
    sorted_students = sorted(valid_students, key=score_key, reverse=True)
    top_students = list(map(add_rank, enumerate(sorted_students[:n], start=1)))
    return top_students, len(valid_students)


def save_result(result, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)


def print_preview(students, n=5):
    print(f"First {n} students:")

    for student in students[:n]:
        print(
            f'ID: {student["student_id"]}, '
            f'Age: {student["age"]}, '
            f'Gender: {student["gender"]}, '
            f'Country: {student["country"]}, '
            f'GPA: {student["GPA"]}'
        )


def print_top_students(top_students):
    print("Top 10 Students by Final Exam Score:")

    for student in top_students:
        print(
            f'{student["rank"]}. '
            f'ID: {student["student_id"]}, '
            f'Country: {student["country"]}, '
            f'Major: {student["major"]}, '
            f'GPA: {student["GPA"]}, '
            f'Final Exam Score: {student["final_exam_score"]}'
        )


def main():
    try:
        print("Practice 5 - Variant D")
        print("Task: get_top_students(students, n=10)")

        input_file = get_input_file()
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        students = load_students(input_file)
        top_10_students, valid_students_count = get_top_students(students, 10)

        result = {
            "practice": "Practice 5",
            "variant": "D",
            "analysis_task": "Top 10 students by final exam score",
            "students_processed": len(students),
            "valid_students_after_filter": valid_students_count,
            "top_10_students": top_10_students,
        }

        save_result(result, OUTPUT_FILE)

        print("Dataset:", os.path.basename(input_file))
        print_preview(students)
        print("Total students:", len(students))
        print("Students after filter:", valid_students_count)
        print("Functions used with filter, sorted, and map: valid_student, score_key, add_rank")
        print_top_students(top_10_students)
        print("JSON file saved to:", OUTPUT_FILE)

    except FileNotFoundError as error:
        print("File error:", error)
    except ValueError as error:
        print("Data conversion error:", error)
    except KeyError as error:
        print("Missing column in CSV file:", error)
    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()