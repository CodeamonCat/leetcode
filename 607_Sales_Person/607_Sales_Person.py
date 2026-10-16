__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame,
                 orders: pd.DataFrame) -> pd.DataFrame:
    company_id = company[company["name"] == "RED"]
    orders = orders[orders["com_id"].isin(company_id["com_id"])]
    return sales_person[~sales_person["sales_id"].isin(orders["sales_id"])][[
        "name"
    ]]
