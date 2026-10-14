__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses.groupby('class').filter(
        lambda x: len(x) >= 5).drop_duplicates(subset=['class']).drop(
            columns=['student']).reset_index(drop=True)
