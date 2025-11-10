import pandas as pd

def load_students_to_df(filepath="data/students.csv"):
    df = pd.read_csv(filepath, converters={'scores': eval})
    return df

def subject_statistics(df, subject):
    df[subject] = df['scores'].apply(lambda x: x.get(subject, 0))
    return {
        "mean": df[subject].mean(),
        "median": df[subject].median(),
        "max": df[subject].max(),
        "min": df[subject].min(),
    }

def filter_top_scorers(df, subject, score_limit=90):
    df[subject] = df['scores'].apply(lambda x: x.get(subject, 0))
    return df[df[subject] >= score_limit][['student_id', 'name', subject]]