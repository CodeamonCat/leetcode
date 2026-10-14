__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = (employee["salary"].drop_duplicates().sort_values(
        ascending=False))
    result = salaries.iloc[N - 1] if N >= 1 and N <= len(salaries) else None

    return pd.DataFrame({f"getNthHighestSalary({N})": [result]})
