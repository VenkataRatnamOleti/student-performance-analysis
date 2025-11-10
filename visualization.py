import matplotlib.pyplot as plt 

def visualize(students):
    if not students:
        print("No data.")
        return

    subjects = set()
    for s in students:
        subjects.update(s.scores.keys())

    for subject in subjects:
        names = [s.name for s in students if subject in s.scores]
        scores = [s.scores.get(subject, 0) for s in students if subject in s.scores]
        plt.figure()
        plt.bar(names, scores)
        plt.title(f"{subject} Scores")
        plt.xlabel("Student")
        plt.ylabel("Score")
        plt.show()

    print("Visualization Completed.")