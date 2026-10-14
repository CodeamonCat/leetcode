__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = (employee["salary"].drop_duplicates().sort_values(
        ascending=False))
    result = salaries.iloc[1] if 2 <= len(salaries) else None

    return pd.DataFrame({f"SecondHighestSalary": [result]})
