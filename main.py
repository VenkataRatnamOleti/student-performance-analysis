from student import Student
import file_ops
import analytics
import visualization
import utils
import analytics_pandas


def menu():
    print()
    print("--------------------------------------------------")
    print("|      Student Performance Analysis System       |")
    print("--------------------------------------------------")
    print("|      1. Add Student Record                     |")
    print("|      2. Display Student Records                |")
    print("|      3. Update Student Record                  |")
    print("|      4. Delete Student Record                  |")
    print("|      5. Search Student                         |")
    print("|      6. Analyze Data                           |")
    print("|      7. Visualize Data                         |")
    print("|      8. Clear Screen                           |")
    print("|      9. Export all data to JSON                |")
    print("|     10. Import all data to JSON                |")
    print("|     11. Save Summary as Text                   |")
    print("|     12. Advanced Pandas Analysis               |")
    print("|     13. Exit                                   |")
    print("--------------------------------------------------")

def main():
    students = file_ops.load_students()

    while True:
        menu()
        choice = input("Enter choice: ")
        utils.clear_console()
        print("--------------------------------------------------")


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
            utils.clear_console()
            continue

        elif choice == "9":
            file_ops.export_to_json(students)
            print("Exported to JSON")

        elif choice == "10":
            students = file_ops.import_from_json()
            print("Imported from JSON")

        elif choice == "11":
            file_ops.save_summary_to_text(students)
            print("Summary written to text file.")

        elif choice == "12":
            df = analytics_pandas.load_students_to_df()
            subject = input("Enter subject for stats: ")
            stats = analytics_pandas.subject_statistics(df, subject)
            print(stats)

        elif choice == "13":
            break

        else:
            print("!!! Invalid option.")

        print("--------------------------------------------------")
        print()


if __name__ == "__main__":
    main()
    utils.clear_console()