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

#recherche les tweets avec le mot macron, en langue française avec un max de 100 tweets retournés par page
#Avec API.Search : ne considère les tweets que des 7 derniers jours
def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

collect()


#recherche les tweets d'un utilisateur identifié par son id
def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

collect_by_user(322)

