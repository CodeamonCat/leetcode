__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def department_highest_salary(employee: pd.DataFrame,
                              department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby("departmentId")["salary"].transform("max")
    result = employee[employee["salary"] == max_salary].merge(
        department,
        left_on="departmentId",
        right_on="id",
        suffixes=("", "_department"),
    )

    return result[[
        "name_department",
        "name",
        "salary",
    ]].rename(columns={
        "name_department": "Department",
        "name": "Employee",
        "salary": "Salary",
    })
