from twitterPredictor.twitter_collect.collect import *


def extract_max_rt(query) :
    """Extrait le tweet avec le plus de RT d'un dataframe de tweets
    :param query : requête utilisée dans l'api.search pour créer la dataframe de tweets
    :return print le tweet avec le plus de RT"""
    data = collect_to_pandas_dataframe(query)
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))


def extract_max_likes(query) :
    """Extrait le tweet avec le plus de Likes d'un dataframe de tweets
    :param query : requête utilisée dans l'api.search pour créer la dataframe de tweets
    :return print le tweet avec le plus de Likes"""
    data = collect_to_pandas_dataframe(query)
    like_max  = np.max(data['Likes'])
    like  = data[data.RTs == like_max].index[0]

    # Max Likes:
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][like]))
    print("Number of retweets: {}".format(like_max))
    print("{} characters.\n".format(data['len'][like]))



def moy_like_rt_candidate(candidate) :
    """Calcule la moyenne de Likes et de RT sur les 200 derniers tweets d'un candidat
    :param candidate : (str) nom du candidat à considérer (cf candidates_id)
    :return : la moyenne des likes, la moyenne des RTs"""
    data = collect_to_pandas_dataframe_user(candidate)
    return(data['Likes'].mean(),data['RTs'].mean())
