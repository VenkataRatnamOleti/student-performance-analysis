def analyze(students):
    if not students:
        print("No data.")
        return

    subjects = set()
    for s in students:
        subjects.update(s.scores.keys())

    for subject in subjects:
        scores = [s.scores.get(subject, 0) for s in students]
        avg = sum(scores) / len(scores)
        top = max(scores)
        print(f"{subject}: Average = {avg:.2f}, Top score = {top}")