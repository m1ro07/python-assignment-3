import csv
import json
import os


INPUT_FILE = "/Users/market/Downloads/global_university_students_performance_habits_10000.csv"
OUTPUT_FOLDER = "/Users/market/Documents/New project/output"
OUTPUT_FILE = "/Users/market/Documents/New project/output/result.json"


class FileManager:
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = output_folder

    def check_file(self):
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"File not found: {self.input_file}")
        print("CSV file found:", self.input_file)

    def create_output_folder(self):
        os.makedirs(self.output_folder, exist_ok=True)
        print("Output folder is ready:", self.output_folder)


class DataLoader:
    def __init__(self, input_file):
        self.input_file = input_file

    def load_data(self):
        students = []

        with open(self.input_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "student_id": row["student_id"],
                    "age": int(row["age"]),
                    "gender": row["gender"],
                    "country": row["country"],
                    "major": row["major"],
                    "GPA": float(row["GPA"]),
                    "final_exam_score": float(row["final_exam_score"]),
                }
                students.append(student)

        print("Data loaded successfully.")
        return students

    def preview_data(self, students, n=5):
        print(f"Preview of first {n} students:")

        for student in students[:n]:
            print(
                f'ID: {student["student_id"]}, '
                f'Age: {student["age"]}, '
                f'Gender: {student["gender"]}, '
                f'Country: {student["country"]}, '
                f'Major: {student["major"]}, '
                f'GPA: {student["GPA"]}, '
                f'Final Exam Score: {student["final_exam_score"]}'
            )


class DataAnalyser:
    def __init__(self, students):
        self.students = students

    def analyse(self):
        return self.get_top_students(10)

    def get_top_students(self, n=10):
        sorted_students = sorted(
            self.students,
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


class ResultSaver:
    def __init__(self, output_file):
        self.output_file = output_file

    def save_to_json(self, result):
        with open(self.output_file, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print("JSON file saved to:", self.output_file)


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
        print("Practice 6 - Week 6: Introduction to OOP")
        print("Variant D")
        print("Analysis task: Top 10 students by final exam score")

        file_manager = FileManager(INPUT_FILE, OUTPUT_FOLDER)
        file_manager.check_file()
        file_manager.create_output_folder()

        data_loader = DataLoader(INPUT_FILE)
        students = data_loader.load_data()
        data_loader.preview_data(students)

        data_analyser = DataAnalyser(students)
        top_10_students = data_analyser.analyse()

        result = {
            "practice": "Practice 6",
            "variant": "D",
            "analysis_task": "Top 10 students by final exam score",
            "students_processed": len(students),
            "top_10_students": top_10_students,
        }

        result_saver = ResultSaver(OUTPUT_FILE)
        result_saver.save_to_json(result)

        print("Dataset:", os.path.basename(INPUT_FILE))
        print("Total students:", len(students))
        print_top_students(top_10_students)
        print("Program finished successfully.")

    except FileNotFoundError as error:
        print(error)
    except ValueError as error:
        print("Data conversion error:", error)
    except KeyError as error:
        print("Missing column in CSV file:", error)
    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()