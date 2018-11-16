import pandas as pd
import matplotlib.pyplot as plt

from twitterPredictor.twitter_collect.collect import *

def graph_Likes_RTs(candidate) :
    """Afficher le graphique montrant l'évolution des Likes et RTs des tweets d'un candidat en fonction du temps
    :param candidate : (str) nom du candidat"""
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


def camembert_2_candidats(candidats) :
    pol,subj,pos,neg,neutre = avis_sur_candidat(candidats[0])
    x1 = [pos,neg,neutre]
    pol,subj,pos,neg,neutre = avis_sur_candidat(candidats[1])
    x2 = [pos,neg,neutre]
    plt.subplot(121)
    plt.title(candidats[0])
    plt.pie(x1, labels = ['Positifs', 'Negatifs', 'Neutre'])
    plt.subplot(122)
    plt.title(candidats[1])
    plt.pie(x2, labels = ['Positifs', 'Negatifs', 'Neutre'])
    plt.show()

import seaborn as sns
from twitterPredictor.tweet_analysis.Analyse_Sentiments import *

def graph_nature_tweets(candidats) :
    #Récupération résultats
    info_candidats = avis_sur_candidats_dataframe(candidats)

    sns.set(style="whitegrid")

    g = sns.catplot(x="Nom_candidat", hue = "pourcentage", data=data,
                height=6, kind="bar", palette="muted")
    g.despine(left=True)

