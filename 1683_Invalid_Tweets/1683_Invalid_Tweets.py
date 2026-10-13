__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets['content'].str.len() > 15][["tweet_id"]]
    # return tweets.loc[tweets['content'].str.len() > 15, ['tweet_id']]
