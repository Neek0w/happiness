import pandas as pd           # Dataframe manipulation
from matplotlib import pyplot as plt # Data visualization
import seaborn as sns         # Data visualization
from plotly.offline import iplot
import plotly.graph_objs as go # plotly graphical object
import warnings
from plotly.offline import plot
warnings.filterwarnings('ignore')

# Lecture du fichier avec le module pandas

data2019 = pd.read_csv("dataSet/2019.csv") # Lire le dataset

# CREATION DE TOUTES LES FONCTIONS

# Création du tableau de corrélation

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

''' 
Nous pouvons s'accorder sur le fait qu'il y a une corrélation entre Happiness Score, 
Economy (GDP per capita), Family (Social support) and Health (Healthy life expectancy).
'''

# Courbe pour démontrer le tableau de corrélation

data_plot = data2019[["Score", "PIB par habitant", "Famille", "Esperance de vie"]]

def corr_sub():
    data_plot.plot(subplots=True)
    data_plot.show()

def corr_all():
    data_plot.plot()
    data_plot.show()

def corr_point():
    data_plot.plot(kind="scatter", x="PIB par habitant", y="Score")
    data_plot.show()

'''Nous pouvons voir la relation positive entre le hapiness score et l'économie du pays '''

# création de la carte

def map ():
    location = pd.read_csv("dataSet/concap.csv") #dataset capitales
    data_new = pd.merge(location[['CountryName', 'CapitalName', 'CapitalLatitude', 'CapitalLongitude']], data2019, left_on='CountryName', right_on='Pays')
    happiness_score = data_new['Score'].astype(float)
    data = [dict(
        type='choropleth',
        colorscale='Rainbow',
        locations=data_new['CountryName'],
        z=happiness_score,
        locationmode='country names',
        text=data_new['Pays'],
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

# Partie sur le Score en général

def score_all():
    plt.figure(figsize=(10, 25))
    sns.barplot(x=data2019['Score'], y=data2019['Pays'])
    plt.xlabel('Score')
    plt.ylabel('Pays')
    plt.title('Score du bonheur')

def score_10er():
    sns.barplot(x=data2019['Score'], y=data2019['Pays'][:10])
    plt.xlabel('Score')
    plt.ylabel('Pays')
    plt.title('Score du bonheur 10 premiers pays')
    plt.show()

def score_10la():
    sns.barplot(x=data2019['Score'], y=data2019['Pays'][-10:])
    plt.xlabel('Score')
    plt.ylabel('Pays')
    plt.title('Score du bonheur 10 derniers pays')
    plt.show()

# Partie sur le PIB par habitant

economie2019 = data2019.sort_values(by=['PIB par habitant'], ascending = False)

def PIB_all():
    plt.figure(figsize=(10, 25))
    sns.barplot(x=economie2019['PIB par habitant'], y=economie2019['Pays'])
    plt.xlabel('PIB par habitant')
    plt.ylabel('Pays')
    plt.title('Classement PIB par habitant par pays')
    plt.show()

def PIB_10er():
    sns.barplot(x=economie2019['PIB par habitant'], y=economie2019['Pays'][:10])
    plt.xlabel('PIB par habitant')
    plt.ylabel('Pays')
    plt.title('Classement PIB par habitant des 10 premiers pays')
    plt.show()

def PIB_10la():
    sns.barplot(x=economie2019['PIB par habitant'], y=economie2019['Pays'][-10:])
    plt.xlabel('PIB par habitant')
    plt.ylabel('Pays')
    plt.title('Classement PIB par habitant des 10 derniers pays')
    plt.show()

# Esperance de Vie

life2019 = data2019.sort_values(by=['Esperance de vie'], ascending = False)

def vie_all():
    plt.figure(figsize=(10, 25))
    sns.barplot(x=life2019['Esperance de vie'], y=life2019['Pays'])
    plt.xlabel('Esperance de vie en bonne santé')
    plt.ylabel('Pays')
    plt.title('Classement esperance de vie par pays')
    plt.show()

def vie_10er():
    sns.barplot(x=life2019['Esperance de vie'], y=life2019['Pays'][:10])
    plt.xlabel('Esperance de vie en bonne santé')
    plt.ylabel('Pays')
    plt.title('Classement esperance de vie des 10 premiers pays')
    plt.show()

def vie_10la():
    sns.barplot(x=life2019['Esperance de vie'], y=life2019['Pays'][-10:])
    plt.xlabel('Esperance de vie en bonne santé')
    plt.ylabel('Pays')
    plt.title('Classement esperance de vie des 10 derniers pays')
    plt.show()

# Partie sur la generosite

gene2019 = data2019.sort_values(by=['Generosite'], ascending = False)

def gene_all():
    sns.barplot(x=gene2019['Generosite'], y=gene2019['Pays'])
    plt.xlabel('Generosite')
    plt.ylabel('Pays')
    plt.title('Classement Generosité 10 premiers pays')
    plt.show()

def gene_10er():
    sns.barplot(x=gene2019['Generosite'], y=gene2019['Pays'][:10])
    plt.xlabel('Generosite')
    plt.ylabel('Pays')
    plt.title('Classement Generosité 10 derniers pays')
    plt.show()

def gene_10la():
    sns.barplot(x=gene2019['Generosite'], y=gene2019['Pays'][-10:])
    plt.xlabel('Generosite')
    plt.ylabel('Pays')
    plt.title('Classement Generosité 10 derniers pays')
    plt.show()

# Partie sur la corruption

corr2019 = data2019.sort_values(by=['Corruption'], ascending = False)

def corr_all():
    plt.figure(figsize=(10, 25))
    sns.barplot(x=corr2019['Corruption'], y=corr2019['Pays'])
    plt.xlabel('Perception de la corruption')
    plt.ylabel('Pays')
    plt.title('Classement perception de la corruption par pays')
    plt.show()

def corr_10er():
    sns.barplot(x=corr2019['Corruption'], y=corr2019['Pays'][:10])
    plt.xlabel('Perception de la corruption')
    plt.ylabel('Pays')
    plt.title('Classement perception 10 premiers par pays')
    plt.show()

def corr_10la():
    sns.barplot(x=corr2019['Corruption'], y=corr2019['Pays'][-10:])
    plt.xlabel('Perception de la corruption')
    plt.ylabel('Pays')
    plt.title('Classement perception de la corruption par pays')
    plt.show()

# Partie sur la Famille

supp2019 = data2019.sort_values(by=['Famille'], ascending = False)

def fam_all():
    plt.figure(figsize=(10, 25))
    sns.barplot(x=supp2019['Famille'], y=supp2019['Pays'])
    plt.xlabel('Support social')
    plt.ylabel('Pays')
    plt.title('Classement du support social par pays')
    plt.show()

def fam_10er():
    sns.barplot(x=supp2019['Famille'], y=supp2019['Pays'][:10])
    plt.xlabel('Support social')
    plt.ylabel('Pays')
    plt.title('Classement du support social des 10 premiers pays')
    plt.show()

def fam_10la():
    sns.barplot(x=supp2019['Famille'], y=supp2019['Pays'][-10:])
    plt.xlabel('Support social')
    plt.ylabel('Pays')
    plt.title('Classement du support social des 10 derniers pays')
    plt.show()

# Partie sur la liberte

free2019 = data2019.sort_values(by=['Liberte'], ascending = False)

def lib_all():
    plt.figure(figsize=(10, 25))
    sns.barplot(x=free2019['Liberte'], y=free2019['Pays'])
    plt.xlabel('liberté de faire des choix')
    plt.ylabel('Pays')
    plt.title('Classement de la liberté par pays')
    plt.show()

def lib_10er():
    sns.barplot(x=free2019['Liberte'], y=free2019['Pays'][:10])
    plt.xlabel('liberté de faire des choix')
    plt.ylabel('Pays')
    plt.title('Classement de la liberté des 10 premiers pays')
    plt.show()

def lib_10la():
    sns.barplot(x=free2019['Liberte'], y=free2019['Pays'][-10:])
    plt.xlabel('liberté de faire des choix')
    plt.ylabel('Pays')
    plt.title('Classement de la liberté des 10 derniers pays')
    plt.show()
