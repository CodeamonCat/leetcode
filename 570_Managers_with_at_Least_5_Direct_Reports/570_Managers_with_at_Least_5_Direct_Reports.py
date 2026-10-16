__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby("managerId").size()
    return employee.loc[employee["id"].isin(managers[managers >= 5].index),
                        ["name"]]
