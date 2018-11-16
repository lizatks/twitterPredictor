def sentiments(text) :
    """renvoie les sentiments d'un texte
    :param text : (str) chaîne de caractère à analyser
    :param langue : (str) langue de text ('EN' pour English)
    :return les sentiments : la polarité et subjectivité du message"""
    wiki = TextBlob(text)
    try :
        return(wiki.translate(to = 'EN').sentiment)
    except :
        return(wiki.sentiment)

hashtags = {"Macron" : "@EmmanuelMacron", "Trump" : "@realDonaldTrump"}

def avis_sur_candidat(candidat) :
    """Renvoie les sentiments sur un candidat en analysant les tweets lui faisant référence
    :param candidat : (str) nom du candidat (cf dictionnaire hastags)
    :return la moyenne de polarité et subjectivité sur les tweets faisant référence au candidat"""
    data = collect_to_pandas_dataframe(hashtags.get(candidat))
    tweets = data['tweet_textual_content']
    n = len(tweets)
    somme_polarity = 0
    somme_subjectivity = 0
    for tweet in tweets :
        somme_polarity, somme_subjectivity = sentiments(tweet)
    return(somme_polarity/n, somme_subjectivity/n)
