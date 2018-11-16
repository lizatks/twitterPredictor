def sentiments(text,langue) :
    """renvoie les sentiments d'un texte
    :param text : (str) chaîne de caractère à analyser
    :param langue : (str) langue de text ('EN' pour English)
    :return les sentiments : la polarité et subjectivité du message"""
    wiki = TextBlob(text)
    if langue == 'EN' :
        return(wiki.sentiment)
    else :
        return(wiki.translate(to = 'EN').sentiment)

