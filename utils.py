import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def search_student(students, sid):
    for s in students:
        if s.student_id == sid:
            return s
    return None

def update_student(students, sid):
    student = search_student(students, sid)
    if student:
        print("Updating student: ", student)
        new_name = input("New name (leave blank to keep): ")
        new_age = input("New age  (leave blank to keep): ")

        if new_name:
            student.name = new_name

        if new_age:
            student.age = int(new_age)

        for subject in student.scores:
            new_score = input(f"New score for {subject} (leave blank to keep): ")
            if new_score:
                student.scores[subject] = int(new_score)
                
    else:
        print("Student not found.")