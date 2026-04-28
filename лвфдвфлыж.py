import csv
import json
import os


DEFAULT_INPUT_FILE = "students.csv"
FALLBACK_INPUT_FILE = "/Users/market/Downloads/global_university_students_performance_habits_10000.csv"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "practice5_result.json")


def valid_student(student):
    return student["final_exam_score"] >= 0

def score_key(student):
    return student["final_exam_score"]

def add_rank(item):
    rank = item[0]
    student = item[1]

    return{
        "rank": rank,
        "student_id": student["student_id"],
        "country": student["country"],
        "major": student["major"],
        "GPA": student["GPA"],
        "final_exam_score": student["final_exam_score"],
    }

class FileManager:
    def __init__(self, input_file, fallback_input_file, output_folder):
        self.input_file = input_file
        self.fallback_input_file = fallback_input_file
        self.output_folder = output_folder

    def get_input_file(self):
        print("FileManager: Checking CSV file...")

        if os.path.exists(self.input_file):
            print("CSV file found:", self.input_file)
            return self.input_file

        if os.path.exists(self.fallback_input_file):
            print("CSV file found:", self.fallback_input_file)
            return self.fallback_input_file

        raise FileNotFoundError("CSV file not found.")

    def create_output_folder(self):
        print("FileManager: creating output folder if needed...")
        os.makedirs(self.output_folder, exist_ok = True)
        print("Output folder is ready:", self.output_folder)

class DataLoader:
    def __init__(self, input_file):
        self.input_file = input_file

    def load_data(self):
        print("DataLoader: reading SCV file...")
        students = []

        with open(self.input_file, "r", encoding = "utf-8", newline ="") as file:
            reader = csv.DictReader(file)
            print("CSV columns:", reader.fieldnames)

            for row in reader:
                students.append(
                    {
                        "student_id": row["student_id"],
                        "age": row["age"],
                        "gender": row["gender"],
                        "country": row["country"],
                        "major": row["major"],
                        "GPA": row["GPA"],
                        "final_exam_score": row["final_exam_score"],
                    }
                )
            print("Data loaded successfully.")
            print("Rows loaded:", len(students))
            return students
    def preview_data(self, students, n = 5):
        print(f'First {n} students:')

        for student in students[:n]:
            print(
                f'ID: {student["student_id"]}',
                f'Age: {student["age"]}',
                f'Gender: {student["gender"]}',
                f'Country: {student["country"]}',
                f'Major: {student["major"]}',
                f'GPA: {student["GPA"]}',
                f'Final Exam Score: {student["final_exam_score"]}'
            )

class DataAnalyser:
    def __init__(self, students):
        self.students = students

    def analyse(self):
        valid_students = list(filter(valid_student, self.students))
        sorted_students = sorted(valid_students, key = score_key, reverse = True)
        top_students = list(map(add_rank, enumerate(sorted_students[:10], start = 1)))
        print(len(top_students))
        return top_students, len(valid_students)

class ResultSaver:
    def __init__(self, output_file):
        self.output_file = output_file
    def save_to_json(self, result):
        with open(self.output_file, "w", encoding = "utf-8") as file:
            json.dump(result, file, indent = 4)

def print_top_students(top_students):

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
        print("=" * 60)
        print("Practice 6 - Variant D")
        print("Topic: Introduction to OOP")
        print("Task: Top 10 students by final exam score")
        print("Required classes: FileManager, DataLoader, DataAnalyser, ResultSaver")
        print("=" * 60)

        file_manager = FileManager(
            DEFAULT_INPUT_FILE,
            FALLBACK_INPUT_FILE,
            OUTPUT_FOLDER,
        )
        input_file = file.manager.get_input_file()
        file_manager.create_output_folder()

        data_loader = DataLoader(input_file)
        students = data_loader.load_data()
        data_loader.preview_data(students)

        data_analyser = DataAnalyser(students)
        top_10_students, valid_student_countr = data_analyser.analyse()


