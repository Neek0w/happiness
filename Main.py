import numpy as np            # Data manipulation
import pandas as pd           # Dataframe manipulation
from matplotlib import pyplot as plt # Data visualization
import seaborn as sns         # Data visualization
import scipy.stats as stats
import chart_studio.plotly as py # visualization library
from plotly.offline import init_notebook_mode # plotly offline mode
from plotly.offline import iplot
import plotly.graph_objs as go # plotly graphical object
import warnings
from plotly.offline import plot
warnings.filterwarnings('ignore')

data2019 = pd.read_csv("dataSet/2019.csv") # Lire le dataset

def tableau_corr():
    f, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(data2019.corr(),
                annot=True,
                linewidths=1,
                cmap="RdBu",
                center=0,
                fmt=".1f",
                square=True
               )

def map ():
    location = pd.read_csv("dataSet/concap.csv") #dataset capitales
    data_new = pd.merge(location[['CountryName', 'CapitalName', 'CapitalLatitude', 'CapitalLongitude']], \
    data2019, left_on='CountryName', right_on='Country or region')
    happiness_score = data_new['Score'].astype(float)
    data = [dict(
        type='choropleth',
        colorscale='Rainbow',
        locations=data_new['CountryName'],
        z=happiness_score,
        locationmode='country names',
        text=data_new['Country or region'],
        colorbar=dict(
            title='Score du Bonheur',
            titlefont=dict(size=25),
            tickfont=dict(size=18))
    )]
    layout = dict(
        title='Score du Bonheur',
        titlefont=dict(size=40),
        geo=dict(
            showframe=True,
            showcoastlines=True,
            projection=dict(type='equirectangular')
        )
    )
    choromap = go.Figure(data=data, layout=layout)
    iplot(choromap, validate=False)
    plot(choromap)

map()