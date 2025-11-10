import csv
import json
from student import Student

DATA_FILE = "data/students.csv"
TEXT_FILE = "data/students.txt"
JSON_FILE = "data/students.json"

def load_students():
    students = []

    try:
        with open(DATA_FILE, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                scores = eval(row['scores'])
                students.append(Student(row['student_id'], row['name'], row['age'], scores))

    except FileNotFoundError:
        pass

    return students

def save_students(students):
    with open(DATA_FILE, mode='w', newline='') as f:
        fieldnames = ['student_id', 'name', 'age', 'scores']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for s in students:
            writer.writerow({'student_id': s.student_id, 'name': s.name, 'age': s.age, 'scores': str(s.scores)})

def save_summary_to_text(students):
    with open(TEXT_FILE, 'w') as f:
        f.write("Student Summary Report\n")
        for s in students:
            f.write(f"ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Total Score: {sum(s.scores.values())}\n")

def export_to_json(students):
    with open(JSON_FILE, 'w') as f:
        json.dump([s.__dict__ for s in students], f)

def import_from_json():
    students = []
    try:
        with open(JSON_FILE, 'r') as f:
            list_dicts = json.load(f)
            for d in list_dicts:
                students.append(Student(d['student_id'], d['name'], d['age'], d['scores']))
    except FileNotFoundError:
        pass

    return students