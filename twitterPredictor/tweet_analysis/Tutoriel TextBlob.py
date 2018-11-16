from textblob import TextBlob

#créer un TextBlob :
wiki = TextBlob("Python is a high-level, general-purpose programming language.")

#accéder aux sentiments: polarity = -1 à 1/ subjectivity = 0 (totalement objectif) à 1 (totalement subjectif)
print(wiki.sentiment)

##si en français : traduire
print(wiki.translate(to = "EN").sentiment)

wiki = TextBlob("I love chocolate")
print(wiki.sentiment)
