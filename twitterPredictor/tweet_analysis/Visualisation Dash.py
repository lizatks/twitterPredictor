import dash
import dash_core_components as dcc
import dash_html_components as html

from twitterPredictor.tweet_analysis.Analyse_Sentiments import *

pol,subj,pos1,neg1,neutre1 = avis_sur_candidat("Macron")
pol,subj,pos2,neg2,neutre2 = avis_sur_candidat("Trump")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='Comparaison Macron Trump',
        figure={
            'data': [
                {'x': ["Macron","Trump"], 'y': [pos1,pos2], 'type': 'bar', 'name': 'Positif'},
                {'x': ["Macron","Trump"], 'y': [neg1,neg2], 'type': 'bar', 'name': u'Négatif'},
                {'x': ["Macron","Trump"], 'y': [neutre1,neutre2], 'type': 'bar', 'name': u'Neutre'}
            ],
            'layout': {
                'title': 'Comparaison Macron Trump'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
