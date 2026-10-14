__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense",
                                          ascending=False).astype(int)
    return scores.drop('id',
                       axis=1).sort_values(by="rank").reset_index(drop=True)
