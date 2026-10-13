__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].str.contains(
        r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$')].sort_values(by="user_id")


users = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5, 6, 7],
    "name": [
        "Winston", "Jonathan", "Annabelle", "Sally", "Marwan", "David",
        "Shapiro"
    ],
    "mail": [
        "winston@leetcode.com", "jonathanisgreat", "bella-@leetcode.com",
        "sally.come@leetcode.com", "quarz#2020@leetcode.com",
        "david69@gmail.com", ".shapo@leetcode.com"
    ]
})

print(valid_emails(users))
