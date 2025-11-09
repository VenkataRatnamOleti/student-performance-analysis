from student import Student
import file_ops
import analytics
import visualization
import utils
import os

def menu():
    print("-----Student Performance Data Analysis System-----")
    print("--------------------------------------------------")
    print("1. Add Student Record")
    print("2. Display Student Records")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Search Student")
    print("6. Analyze Data")
    print("7. Visualize Data")
    print("8. Clear Screen")
    print("9. Exit")
    print("--------------------------------------------------")

def main():
    students = file_ops.load_students()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            student = Student.from_input()
            students.append(student)
            file_ops.save_students(students)

        elif choice == "2":
            for s in students:
                print(s)

        elif choice == "3":
            sid = input("Enter student ID to update: ")
            utils.update_student(students, sid)
            file_ops.save_students(students)

        elif choice == "4":
            sid = input("Enter student ID to delete: ")
            students = [s for s in students if s.student_id != sid]
            file_ops.save_students(students)

        elif choice == "5":
            sid = input("Enter student ID to search: ")
            student = utils.search_student(students, sid)
            print(student if student else "Not found")

        elif choice == "6":
            analytics.analyze(students)

        elif choice == "7":
            visualization.visualize(students)

        elif choice == "8":
            os.system('cls')

        elif choice == "9":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()