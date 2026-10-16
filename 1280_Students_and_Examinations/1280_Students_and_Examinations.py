__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    result = students.merge(subjects, how="cross").merge(
        examinations.groupby(["student_id", "subject_name"
                              ]).size().reset_index(name="attended_exams"),
        on=["student_id", "subject_name"],
        how="left").sort_values(by=["student_id", "subject_name"]).reset_index(
            drop=True)
    result["attended_exams"] = result["attended_exams"].fillna(0)
    return result
