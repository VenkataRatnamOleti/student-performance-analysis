class Student:
    def __init__(self, student_id, name, age, scores):
        self.student_id = student_id
        self.name = name
        self.age = int(age)
        self.scores = scores   # Dict {subject: score}


    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Scores: {self.scores}"

    def from_input():
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        scores = {}

        while True:
            subject =  input("Enter subject (blank to finist): ")
            if not subject:
                break

            score = int(input(f"Score for {subject}: "))
            scores[subject] = score

        return Student(student_id, name, age, scores)