import pandas as pd
import matplotlib.pyplot as plt

from twitterPredictor.twitter_collect.collect import *

collect_to_pandas_dataframe_user("Macron")

def graph_Likes_RTs(candidate) :
    data = collect_to_pandas_dataframe_user(candidate)

    tfav = pd.Series(data['Likes'].values, index=data['Date'])
    tret = pd.Series(data['RTs'].values, index=data['Date'])

    plt.figure()
    # Likes vs retweets visualization:
    #tfav.plot(figsize=(16,4), label="Likes", legend=True)
    #tret.plot(figsize=(16,4), label="Retweets", legend=True)

    plt.plot(tfav, label="Likes")
    plt.plot(tret, label="Retweets")
    plt.legend()

    plt.show()
