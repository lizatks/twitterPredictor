import tweepy
import json

from twitterPredictor.twitter_collect.collect import *

def store_tweets(tweets, candidate) :
    """Enregistre les tweets (leur id, texte et date) sous formats json après sérialisation
    :param tweets : résultat d'une recherche de type api.search
    :param candidate : nom du candidat  qui sera le nom du fichier à créer dans lequel on enregistrera les tweets
    :return création du fichier filename"""

    list_dico = []
    for tweet in tweets :
        dico = {}
        dico["id"] = tweet.id
        dico["text"] = tweet.text
        dico["created_at"] = str(tweet.created_at) #type datetime non reconnu par json
        #dico["hastags"] = tweet.entities.hashtags : plus compliqué tweet.entities.get("hashtags")[0].get("text") ???
        list_dico.append(dico)
    with open(candidate + ".json", 'w', encoding='utf-8') as f :
        json.dump(list_dico, f, indent=4)


