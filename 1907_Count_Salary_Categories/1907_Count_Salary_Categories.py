__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    result = pd.cut(accounts["income"],
                    bins=[-float("inf"), 19999, 50000,
                          float("inf")],
                    labels=["Low Salary", "Average Salary", "High Salary"])
    return result.value_counts().rename_axis("category").reset_index(
        name="accounts_count")
