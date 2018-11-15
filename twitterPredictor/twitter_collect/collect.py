import tweepy

# We import our access keys:
from twitterPredictor.credentials import *

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

CANDIDATES = {1 : "Macron", 2 : "EP"}

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    list_queries = []
    try:
        texte = file_path + "_candidate_" + CANDIDATES[num_candidate] + ".txt"
        with open("""C:/Users/Kumquat/Documents/Git/Twitter/twitterPredictor/CandidateData/""" + texte, "r") as fichier :
            query = ""
            data = fichier.read()

            for i in range(len(data)-1) : # "-1" pour ne pas avoir le retour à la ligne = \n
                if data[i] == "," :
                    list_queries.append(query)
                    query = ""
                    i += 1
                else :
                    query += data[i]
            list_queries.append(query)

        return(list_queries)

    except IOError:
        return("Nom de fichier incorrect")


def get_tweets_from_candidates_search_queries(queries, twitter_api) :
    """Renvoie les tweets correspondants aux mots clés ou hashtags
    :param queries: list of string queries = liste de requêtes à utiliser avec api.search
    :param twitter_api: instance de connection
    :return liste de tweets(json)"""
    list_tweets = []
    try :
        connexion = twitter_api
        list_tweets = []
        for query in queries :
            tweets = connexion.search(query,language="french",rpp=10)
            list_tweets.append(tweets)
        return(list_tweets)
    except tweepy.TweepError :
        return("Erreur avec Twitter")
    except tweepy.RateLimitError :
        return("Atteinte taux limite de Twitter")


def main_collect() :
    """Renvoie les tweets des 2 candidats considérés
    :return liste (list) des listes (list) contenant les tweets (json) pour les 2 candidats"""
    list_num_candidate = [1,2]
    list_file_path = ["keywords","hashtag"]
    twitter_api = twitter_setup()
    list_tweets_candidates = []

    for i in list_num_candidate :
        print(type(get_candidate_queries(i,list_file_path[0])))
        print(type(get_candidate_queries(i,list_file_path[1])))
        list_queries = get_candidate_queries(i,list_file_path[0]) + get_candidate_queries(i,list_file_path[1])
        list_tweets_candidates.append(get_tweets_from_candidates_search_queries(list_queries,twitter_api))

    return(list_tweets_candidates)

