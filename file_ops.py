import csv
from student import Student

DATA_FILE = "data/students.csv"

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