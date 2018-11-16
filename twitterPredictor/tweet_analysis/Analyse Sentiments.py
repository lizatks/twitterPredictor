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
    :return la moyenne de polarité et subjectivité sur les tweets faisant référence au candidat, le pourcentage de tweets positifs, négatifs et neutres"""
    data = collect_to_pandas_dataframe(hashtags.get(candidat))
    tweets = data['tweet_textual_content']
    n = len(tweets)
    somme_polarity = 0
    somme_subjectivity = 0
    nb_pos = 0
    nb_neg = 0
    nb_neutre = 0
    for tweet in tweets :
        pol,subj = sentiments(tweet)
        somme_polarity += pol
        somme_subjectivity += subj
        if pol > 0 :
            nb_pos += 1
        elif pol < 0 :
            nb_neg +=1
        else :
            nb_neutre +=1
    print('a')
    return(somme_polarity/n, somme_subjectivity/n, nb_pos/n, nb_neg/n, nb_neutre/n)


