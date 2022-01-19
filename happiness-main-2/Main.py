import pandas as pd           # Dataframe manipulation
from matplotlib import pyplot as plt # Data visualization
import seaborn as sns         # Data visualization
from plotly.offline import iplot
import plotly.graph_objs as go # plotly graphical object
import warnings
from plotly.offline import plot
warnings.filterwarnings('ignore')
from tkinter import *

# Lecture du fichier avec le module pandas

data2019 = pd.read_csv("dataSet/2019.csv") # Lire le dataset

# CREATION DE TOUTES LES FONCTIONS

# Création du tableau de corrélation

def tableau_corr():
    f, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(data2019.corr(),
                annot=True,
                linewidths=1,
                cmap="RdBu",
                center=0,
                fmt=".1f",
                square=True
                )
    plt.show()

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
    plt.show()
# Partie sur le Score en général

def score():
    if nbr_choix == 0:
        plt.figure(figsize=(10, 25))
        sns.barplot(x=data2019['Score'], y=data2019['Pays'])
        plt.xlabel('Score')
        plt.ylabel('Pays')
        plt.title('Score du bonheur')
        plt.show()
    if nbr_choix == 1:
        score_10er()
    if nbr_choix == 2:
        score_10la()


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
    plt.figure(figsize=(10, 7))
    sns.barplot(x=supp2019['Pays'], y=supp2019['Famille'])
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


nbr_choix=0
def er ():
    nbr_choix = 1
def la():
    nbr_choix = 2





def w1():
    #tkinter fenetre
    w = Tk()
    w.title("Menu")
    w.geometry("900x680")
    w.minsize(480,300)
    w.config(background="#41B77F")

    #creer la frame gros bouton
    frame = Frame(w,bg="#41B77F")

    #ajouter texte
    title_ = Label(frame,text="Bienvenue sur notre pojet SAE15",font=("Courrier",45),bg="#41B77F")
    title_.pack() #affiche notre texte

    #ajouter 2eme texte
    title_ = Label(frame,text="cliquez sur l'option que vous choisissez",font=("Courrier",25),bg="#41B77F")
    title_.pack()

    #creer bouton map
    map_bouton = Button(frame,text="map interactive",font=("Courrier",35),command=map,bg="#41B77F",fg="black")
    map_bouton.pack(pady=20,fill=X)

    #creer bouton correlation
    corr_b = Button(frame,text="table de correlation ",font=("Courrier",35),command=tableau_corr,bg="#41B77F",fg="black")
    corr_b.pack(pady=20,fill=X)

    choix_b = Button(frame,text="choisir ses options ",font=("Courrier",35),command=w2,bg="#41B77F",fg="black")
    choix_b.pack(pady=20,fill=X,side=BOTTOM)

    fermer = Button(w, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#41B77F", fg="#41B77F")
    fermer.pack(pady=20, fill=X, side=BOTTOM)



    #activer laffichage (frame)
    frame.pack(expand=True)
    #afficher
    w.mainloop()


def w2():
    w2 = Tk()
    w2.title("menu parametre")
    w2.geometry("900x680")
    w2.minsize(480, 300)
    w2.config(background="#41B77F")

    frame2= Frame(w2,bg="#41B77F")
    frame3= Frame(w2,bg="#41B77F")

    title_ = Label(frame2, text="Bienvenue sur notre pojet SAE15", font=("Courrier", 45), bg="#41B77F")
    title_.pack(pady=20)
    title_ = Label(frame3, text="Selectionner l'option permettant de faire ", font=("Courrier", 25), bg="#41B77F")
    title_bis = Label(frame3, text="votre classement en cliquant dessus ", font=("Courrier", 25), bg="#41B77F")
    title_.pack()
    title_bis.pack()
    _er = Button(frame3, text="10 premiers", font=("Courrier", 20), command=w_er, bg="#41B77F", fg="black")
    _la = Button(frame3, text="10 derniers", font=("Courrier", 20), command=w_la, bg="#41B77F", fg="black")
    _er.pack(side=LEFT,pady=20)
    _la.pack(side=RIGHT,pady=20)
    fermer = Button(w2, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#41B77F", fg="#41B77F")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    rtr = Button(w2, text="retour",font=("Courrier", 10), command=w1, bg="#41B77F", fg="#41B77F" )
    rtr.place(x=0, y=0)

    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    w2.mainloop()


def w_er():
    w_er = Tk()
    w_er.title("menu parametre")
    w_er.geometry("900x680")
    w_er.minsize(480, 300)
    w_er.config(background="#41B77F")

    frame2 = Frame(w_er, bg="#41B77F")
    frame3 = Frame(w_er, bg="#41B77F")

    rtr = Button(w_er, text="retour", font=("Courrier", 10), command=w2, bg="#41B77F", fg="#41B77F")
    rtr.place(x=0, y=0)
    fermer = Button(w_er, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#41B77F", fg="#41B77F")
    fermer.pack(pady=20, fill=X, side=BOTTOM)

    title_ = Label(frame3, text="Choisissez votre parametre", font=("Courrier", 35), bg="#41B77F")
    title_.pack(pady=20)

    bscore = Button(frame3,text="Score du bonheur",font=("courrier",20),command=score_10er, bg="#41B77F", fg="black")
    bscore.pack(pady=7, fill=X)
    bpib = Button(frame3, text="PIB du pays", font=("courrier", 20), command=PIB_10er, bg="#41B77F", fg="black")
    bpib.pack(pady=7, fill=X)
    bvie = Button(frame3, text="Moyenne de longevité", font=("courrier", 20), command=vie_10er, bg="#41B77F", fg="black")
    bvie.pack(pady=7, fill=X)
    bgene = Button(frame3, text="Score de generosité", font=("courrier", 20), command=gene_10er, bg="#41B77F", fg="black")
    bgene.pack(pady=7, fill=X)
    bcorr = Button(frame3, text="Corruption au sein du pays", font=("courrier", 20), command=corr_10er, bg="#41B77F", fg="black")
    bcorr.pack(pady=7, fill=X)
    bfam = Button(frame3, text="importance de la famille", font=("courrier", 20), command=fam_10er, bg="#41B77F", fg="black")
    bfam.pack(pady=7, fill=X)
    blib = Button(frame3, text="liberté de ses choix", font=("courrier", 20), command=lib_10er, bg="#41B77F", fg="black")
    blib.pack(pady=7, fill=X)

    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    w_er.mainloop()

def w_la():
    w_la = Tk()
    w_la.title("menu parametre")
    w_la.geometry("900x680")
    w_la.minsize(480, 300)
    w_la.config(background="#41B77F")

    frame2 = Frame(w_la, bg="#41B77F")
    frame3 = Frame(w_la, bg="#41B77F")

    rtr = Button(w_la, text="retour", font=("Courrier", 10), command=w2, bg="#41B77F", fg="#41B77F")
    rtr.place(x=0, y=0)
    fermer = Button(w_la, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#41B77F", fg="#41B77F")
    fermer.pack(pady=20, fill=X, side=BOTTOM)

    title_ = Label(frame3, text="Choisissez votre parametre", font=("Courrier", 35), bg="#41B77F")
    title_.pack(pady=20)

    bscore = Button(frame3,text="Score du bonheur",font=("courrier",20),command=score_10la, bg="#41B77F", fg="black")
    bscore.pack(pady=7, fill=X)
    bpib = Button(frame3, text="PIB du pays", font=("courrier", 20), command=PIB_10la, bg="#41B77F", fg="black")
    bpib.pack(pady=7, fill=X)
    bvie = Button(frame3, text="Moyenne de longevité", font=("courrier", 20), command=vie_10la, bg="#41B77F", fg="black")
    bvie.pack(pady=7, fill=X)
    bgene = Button(frame3, text="Score de generosité", font=("courrier", 20), command=gene_10la, bg="#41B77F", fg="black")
    bgene.pack(pady=7, fill=X)
    bcorr = Button(frame3, text="Corruption au sein du pays", font=("courrier", 20), command=corr_10la, bg="#41B77F", fg="black")
    bcorr.pack(pady=7, fill=X)
    bfam = Button(frame3, text="importance de la famille", font=("courrier", 20), command=fam_10la, bg="#41B77F", fg="black")
    bfam.pack(pady=7, fill=X)
    blib = Button(frame3, text="liberté de ses choix", font=("courrier", 20), command=lib_10la, bg="#41B77F", fg="black")
    blib.pack(pady=7, fill=X)

    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    w_er.mainloop()


w1()



