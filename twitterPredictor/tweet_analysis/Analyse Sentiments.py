def sentiments(text,langue) :
    """renvoie les sentiments d'un texte
    :param text : (str) chaîne de caractère à analyser
    :param langue : (str) langue de text ('EN' pour English)
    :return les sentiments : la polarité et subjectivité du message"""
    wiki = TextBlob(text)
    if langue == 'EN' :
        return(wiki.sentiment)
    else :
        try :
            return(wiki.translate(to = 'EN').sentiment)
        except :
            return(wiki.sentiment)

def avis_sur_candidat(candidat, langue) :
    data = collect_to_pandas_dataframe("@" + candidat)
    tweets = data['tweet_textual_content']
    n = len(tweets)
    somme_polarity = 0
    somme_subjectivity = 0
    for tweet in tweets :
        somme_polarity, somme_subjectivity = sentiments(tweet,langue)
    return(somme_polarity/n, somme_subjectivity/n)
