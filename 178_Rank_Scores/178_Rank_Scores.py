__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense",
                                          ascending=False).astype(int)
    return scores.drop('id', axis=1).sort_values('rank').reset_index(drop=True)


scores = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65],
})

print(order_scores(scores))
