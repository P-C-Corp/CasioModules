﻿# -*- coding: utf-8 -*-
#
"""
Le module lycee est un module python réalisé par le groupe AMIENS PYTHON
est à pour objectif de simplifier un certain nombre de manipulations
avec python au lycée (cosinus en degré, calcul d'une moyenne d'une liste,
représentation statistiques variées, ...)

Pour l'utiliser, il suffit d'ajouter en début de programme

from lycee import *
"""
import math
import random as alea
import matplotlib.pyplot as plt
import numpy as np
__version__ = '2.6'
pi=math.pi
AlphabetAP=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?&àâéèêëîïù#'(-_){}[]|\@=+°§$<>%*/"





# -------------------------------------------------------
#    FONCTIONS STAT & PROBAS
# -------------------------------------------------------
def randint(min,max):
    """
    min et max sont deux entiers.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un entier choisi de manière (pseudo)aléatoire et équiprobable
    dans l'intervalle [min,max].
    """
    return alea.randint(min,max)

def choice(list):
    """
    list est une liste.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un élément de la liste list choisi (pseudo)aléatoirement et de manière équipropable
    """
    return alea.choice(list)

def random():
    """
    Pas d'argument.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie au hasard un décimal de l'intervalle [0;1[
    """
    return alea.random()

def uniform(min,max):
    """
    min et max sont deux nombres.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un nombre décimal choisi de manière (pseudo)aléatoire et
    uniforme de l'intervalle [min,max[.
    """
    return alea.uniform(min,max)

def intervalle(debut,fin,n=500):
    """
    debut, fin et pas sont des nombres.
    Le paramètre n est optionnel (500 par défaut).
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne une liste de n nombres équirépartis dans l'intervalle [debut, fin]
    """
    return list(np.linspace(debut, fin, n))





# -------------------------------------------------------
#    FONCTIONS SUR NUMPY
# -------------------------------------------------------
def vecteur(x,y,z='optionel'):
    """
    x et y sont des nombres
    z est un nombre optionel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un vecteur de coordonées (x,y) ou (x,y,z)
    """
    if z=='optionel':
        return np.array([x,y])
    else :
        return np.array([x,y,z])

def norme(v):
    """
    v est un vecteur du plan ou de l'espace
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie la norme du vecteur v
    """
    l=v*v;n=0
    for i in range(len(l)) : n=n+l[i]
    return sqrt(n)

def abscisse(v):
    """
    v est un vecteur du plan ou de l'espace
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie l'abscisse du vecteur v
    """
    return v[0]

def ordonnee(v):
    """
    v est un vecteur du plan ou de l'espace
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie l'ordonnée du vecteur v
    """
    return v[1]

def cote(v):
    """
    v est un vecteur de l'espace
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie la cote du vecteur v
    """
    return v[2]


# -------------------------------------------------------
#    FONCTIONS DIAGRAMME STAT
# -------------------------------------------------------

def baton(xi,ni='optionnel',couleur='optionnel'):
    """
    xi est une liste de valeurs
    ni est la liste des effectifs associés, c'est un paramètre optionnel.
    couleur donne la couleur du diagramme (optionnel)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génére le diagramme en bâtons relatif à la liste.
    """
    if couleur=='optionnel' : couleur='b'
    if type(ni) != list:
        xi,ni=compte(xi,'effectif')
    repere.title('Diagramme en bâtons de la liste')
    repere.ylabel('Effectifs')
    repere.xlabel('Valeurs de la liste')
    for i in range(len(xi)):
        repere.plot([xi[i],xi[i]],[0,ni[i]],couleur,lw=2)
    repere.axis([min(xi)-0.1, max(xi)+0.1,0,max(ni)])

def histop(Liste,Classes='optionnel') :
    """
    Liste est une liste de valeurs
    Si seulement Liste est renseigné, les valeurs seront réparties en 10 classes.
    Si Classes est un entier, les valeurs seront réparties en ce nombre de classes.
    Sinon, vous pouvez choisir vos classes d'amplitudes variées
        en indiquant comme Classes    la liste ordonnée des bornes.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génère l'histogramme relatif à la Liste d'aire totale 1.
    """
    C=Classes
    if C=='optionnel' : C = 10
    if type(C) == int :
        pas=(max(Liste)-min(Liste))/C
        a=min(Liste)
        C=[]
        while a<=max(Liste) :
            C.append(a)
            a=a+pas
    Eff=[0]*(len(C)-1)
    for v in Liste :
        i=0
        while i<len(C)-1 :
            if v>=C[i] and (v<C[i+1] or (i==len(C)-2 and v==C[i+1])) :
                Eff[i]=Eff[i]+1
                i=len(C)
            else :
                i=i+1
    taille=[C[i+1]-C[i] for i in range(len(C)-1)]
    TotalEff = sum(Eff)
    H=[Eff[i]/(taille[i]*TotalEff) for i in range(len(C)-1)]
    repere.bar(C[:-1],H,width=taille)
    n=int(len(Liste)/(len(C)-1)/5)
    if n==0 : n=1
    if n>9 :
        d=int(ln(n)/ln(10))-1
        n=int(round(n*(10**(-d))))*10**d
    xi,ni=compte(taille,'effectif')
    m=max(ni)
    l,i=0,0
    while l==0 :
        if ni[i]==m :
            l=xi[i]
        else :
            i=i+1
    for i in range(len(taille)) :
        if taille[i] == l and Eff[i] !=0 :
           h=H[i]*n/Eff[i]
    xc=C[0]
    yc=max(H)*1.1
    repere.plot([xc,xc+l],[yc,yc],'b')
    repere.plot([xc,xc+l],[yc+h,yc+h],'b')
    repere.plot([xc,xc],[yc,yc+h],'b')
    repere.plot([xc+l,xc+l],[yc,yc+h],'b')
    txt=" "+str(n)+" individu"
    if n>1 : txt=txt+"s"
    txt=txt+", soit "+str(round(n/len(Liste)*10000)/100)+"% de la population"
    repere.text(xc+l*1.1,yc+h/2,txt,verticalalignment='center')


def barre(Liste,a='optionnel',pas='optionnel') :
    """
    Liste est une liste de valeurs
    Si seulement Liste est renseigné, les valeurs seront réparties en 10 classes.
    Si Liste et a sont renseignés, les valeurs seront réparties en a classes.
    Si les trois paramètres sont renseignés:
            a est le centre de la première classe,
            et pas est l'amplitude des classes.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génère le diagramme en barres relatif à la Liste.
    """
    if pas=='optionnel' :
        if a=='optionnel' : a=10
        repere.hist(Liste,bins=a)
    else :
        n=a-pas/2
        C=[]
        while n<max(Liste)+pas :
            C.append(n)
            n=n+pas
        Eff=[0]*(len(C)-1)
        for v in Liste :
            i=0
            while i<len(C)-1 :
                if v>=C[i] and v<C[i+1] or (i==len(C)-2 and v==C[i+1]) :
                    Eff[i]=Eff[i]+1
                    i=len(C)
                else :
                    i=i+1
        repere.bar(C[:-1],Eff,width=pas)

def compte(liste,option='optionnel'):
    """
    liste est une liste de nombres
    option est un paramètre optionnel: "frequence" , "effectif"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne la liste triée sans les doublons et
      – Si l'option est "effectif", la liste est retournée avec les effectifs des valeurs.
      – Si l'option est "frequence", la liste est retournée avec les fréquences des valeurs.
    """
    def divliste(x):                            #Définition de la fonction pour diviser par l'effectif total
        return x/len(liste)
    liste=sorted(liste)                         #On trie la liste pour rencontrer les éléments par ordre croissant.
    listf=[liste[0]]                            #Initialise la liste des valeurs avec la première valeur
    eff=[liste.count(liste[0])]                 #Initialise la liste des effectifs avec le premier effectif associé
    for i in range(len(liste)):                 #On parcourt la série
        if liste[i] not in listf:
            listf.append(liste[i])              #Si l'élément n'a pas encore été rencontré, il est ajouté à la liste.
            eff.append(liste.count(liste[i]))   #Ajoute à la liste des effectifs, l'effectif associé à cette nouvelle valeur
    if option=='effectif':
        return sorted(listf),eff
    elif option=='frequence' or option=='frequences':
        return sorted(listf),list(map(divliste,eff))  #Calcul des fréquences par division par l'effectif total.
    else:
        return sorted(listf)


def listeRand(n):
    """
    n est est un nombre
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne une liste de n nombres décimaux aléatoires dans l'intervalle [ 0, 1[.
    """
    if n==0:
        return []
    else:
        list=[]
        for i in range(n):
              list.append(random())
        return list

def listeRandint(min,max,n):
    """
    min est un nombre
    max est un nombres
    n est est un nombre
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne une liste de n nombres entiers aléatoires dans l'intervalle [min , max].
    """
    if n==0:
        return []
    else:
        list=[]
        for i in range(n):
              list.append(randint(min,max))
        return list

def centres(L):
    """
    L est une liste de taille n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie une liste de longueur n-1 contenant les valeurs (L[i]+L[i+1])/2.
    """
    R=[]
    for i in range(len(L)-1):
        R.append((L[i]+L[i+1])/2)
    return R

def ECC(xi,ni='optionnel'):
    """
    xi est une liste de valeurs
    ni est la liste des effectifs associés, c'est un paramètre optionnel.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génère les effectifs cumulés croissants d'une liste.
    """
    if ni=='optionnel': xi,ni=compte(xi,'effectif')
    T=0;E=[]
    for i in range(len(ni)):
        T=T+ni[i]
        E.append(T)
    return xi,E

def FCC(xi,ni='optionnel'):
    """
    xi est une liste de valeurs
    ni est la liste des effectifs associés, c'est un paramètre optionnel.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génère les fréquences cumulées croissantes d'une liste.
    """
    xi,ni=ECC(xi,ni)
    for i in range(len(ni)) : ni[i]=ni[i]/ni[len(ni)-1]
    return xi,ni

def polygoneECC(xi,ni='optionnel',couleur='b'):
    """
    xi est une liste de valeurs
    ni est la liste des effectifs associés, c'est un paramètre optionnel.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génére le polygone des Effectifs cumulés croissants de la liste
    """
    xi,ec=ECC(xi,ni)
    if len(xi)==len(ec)+1 :
        ec.insert(0,0)
        repere.plot(xi,ec,couleur+'o')
        repere.plot(xi,ec,couleur)
        repere.title('Polygone des Effectifs Cumules Croissants')
        repere.ylabel('Effectifs')
        repere.xlabel('Valeurs de la liste')

def polygoneFCC(xi,ni='optionnel',couleur='b'):
    """
    xi est une liste de valeurs
    ni est la liste des effectifs associés, c'est un paramètre optionnel.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Génére le polygone des fréquences cumulées croissantes de la liste
    """
    xi,ec=FCC(xi,ni)
    if len(xi)==len(ec)+1 :
        ec.insert(0,0)
        repere.plot(xi,ec,couleur+'o')
        repere.plot(xi,ec,couleur)
        repere.title("Polygone des frequences cumulees Croissantes")
        repere.ylabel('Frequences')
        repere.xlabel('Valeurs de la liste')


def moyenne(xi,ni='optionnel'):
    """
    xi est une série de valeurs (ou les extrémité des classes)
    ni est la série des effectifs associés (optionnelle)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie la moyenne de la liste
    """
    if ni=='optionnel' : xi,ni=compte(xi,'effectif')
    if len(xi)==len(ni)+1 : xi=centres(xi) # Si on travaille avec des classes
    s=0
    #print xi,ni
    for i in range(len(xi)):
        s=s+xi[i]*ni[i]
    return s/sum(ni)

def mediane(xi,ni='optionnel',option='optionel'):
    """
    xi est une série de valeurs
    ni est la série (optionnelle) des effectifs associés
    option est un paramètre optionnel: 1 ou 2
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie la médiane de la liste
    - L'option par défaut est l'option 1.
    - Si l'option est 1, la médiane est la valeur centrale (valeur de la série ou moyenne arithmétique)
    - Si l'option est 2, la médiane est la valeur pour laquelle on dépasse 50% des valeurs.

    """
    if ni=='optionnel':                     #On vérifie si ni existe
        xi,ni=compte(xi,'effectif')
    elif ni==2 or ni==1:                    #On vérifie si option existe
        option=ni
        xi,ni=compte(xi,'effectif')
    else:                                   #ni existe, on vérifie si xi est ordonnée sinon on trie xi et ni
        if xi != sorted(xi) and type(ni) == list:
            xi,ni=trier_liste(xi,ni)
    i=0
    k=ni[0]
    while k<sum(ni)/2:
        i=i+1
        k=k+ni[i]
    if option==2:   #Option 2
        if k<=sum(ni)/2:
            return xi[i+1]
        else:
            return xi[i]
    else:           #Option 1 par défaut
        if sum(ni) % 2 == 0:
            if k<=sum(ni)/2:
                return (xi[i]+xi[i+1])/2
            else:
                return xi[i]
        else:
            if k<=sum(ni)/2:
                return xi[i+1]
            else:
                return xi[i]

def quartile(xi,ni='optionnel',valeur='optionnel'):
    """
    xi est une série de valeurs
    ni est la série des effectifs associés (optionnelle)
    valeur est le quartile que l'on souhaite 1 ou 3 (optionnelle)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne les quartiles de la liste.
    - Si valeur=1, retourne le premier quartile.
    - Si valeur=3, retourne le troisième quartile.
    - Par défaut, le premier et le troisième quartile sont retournés
    """
    if ni=='optionnel':                     #On vérifie si ni existe
        xi,ni=compte(xi,'effectif')
    elif ni==3 or ni==1:                    #On vérifie si valeur existe
        valeur=ni
        xi,ni=compte(xi,'effectif')
    else:                                   #ni existe, on vérifie si xi est ordonnée sinon on trie xi et ni
        if xi != sorted(xi) and type(ni)==list:
            xi,ni=trier_liste(xi,ni)
    q1pos = sum(ni) //4                   #On définit la position de q1
    q3pos = (3*sum(ni)) //4                 #On définit la position de q3
    k = ni[0]
    i = 0
    while k < q1pos:                          #On cherche q1
        i = i+1
        k = k+ni[i]
    q1 = xi[i]                                #On définit q1
    while k<q3pos:                          #On cherche q3
        i=i+1
        k=k+ni[i]
    q3=xi[i]                                #On définit q3
    if valeur==1:                           #Affichage du 1er quartile
        return q1
    if valeur==3:                           #Affichage du 3ème quartile
        return q3
    if valeur != 1 and valeur != 3:             #Option par défaut
        return q1,q3

    q1=liste[len(liste)//4]
    q3=liste[3*len(liste)//4]
    if valeur==1:
        return q1
    elif valeur==3:
        return q3
    else:
        return q1,q3

def decile(xi,ni='optionnel',valeur='optionnel'):
    """
    xi est une série de valeurs
    ni est la série des effectifs associés (optionnelle)
    valeur est le decile que l'on souhaite 1 ou 9 (optionnelle)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne les déciles de la liste.
    - Si valeur=1, retourne le premier décile.
    - Si valeur=9, retourne le neuvième décile.
    - Par défaut, le premier et le neuvième décile sont retournés
    """
    if ni=='optionnel':                     #On vérifie si ni existe
        xi,ni=compte(xi,'effectif')
    elif ni==9 or ni==1:                    #On vérifie si valeur existe
        valeur=ni
        xi,ni=compte(xi,'effectif')
    else:                                   #ni existe, on vérifie si xi est ordonnée sinon on trie xi et ni
        if xi != sorted(xi) and type(ni)==list:
            xi,ni=trier_liste(xi,ni)

    d1pos=int(sum(ni)/10)                   #On définit la position de d1
    d9pos=int(9*sum(ni)/10)                 #On définit la position de d9
    k=0
    i=0
    while k<d1pos:                          #On cherche d1
        k=k+ni[i]
        i=i+1
    d1=xi[i]                                #On définit d1
    while k<d9pos:                          #On cherche d19
        k=k+ni[i]
        i=i+1
    d9=xi[i]                                #On définit d9
    if valeur==1:                           #Affichage du 1er décile
        return d1
    if valeur==9:                           #Affichage du 9eme décile
        return d9
    if valeur != 1 and valeur != 9:             #Option par défaut
        return d1,d9

def variance(xi,ni='optionnel'):
    """
    xi est une série de valeurs (ou les extrémité des classes)
    ni est la série des effectifs associés (optionnelle)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne la variance de la liste.
    """
    if type(ni) != list:
        xi,ni=compte(xi,'effectif')
    if len(xi)==len(ni)+1 : xi=centres(xi) # Si on travaille avec des classes
    v=0
    xbar=moyenne(xi,ni)
    for i in range(len(xi)):
        v=v+(xi[i]-xbar)**2*ni[i]
    return v/(sum(ni))


def ecartype(xi,ni='optionnel'):
    """
    xi est une série de valeurs (ou les extrémité des classes)
    ni est la série des effectifs associés (optionnelle)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne l'écart-type de la liste
    """
    return sqrt(variance(xi,ni))


#----------------------------------------------------------
# Nouvelles fonctions EduPython 2.0 (2.1 en fait)
#----------------------------------------------------------


def uniform(min,max):
    """
    min et max sont deux nombres.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un nombre décimal choisi de manière (pseudo)aléatoire et
    uniforme de l'intervalle [min,max[.
    """
    return alea.uniform(min,max)

def tirageBinomial(n,p) :
    """
    n et p sont les paramètres de la loi binomiale à simuler.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un nombre entier choisi de manière aléatoire selon
    une loi de binomiale B(n,p).
    """
    s = 0
    for i in range(n) :
        if random()<p :
            s = s + 1
    return s


def expovariate(l):
    """
    l est un réel strictement positif.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un nombre réel choisi de manière aléatoire
    selon une loi exponentielle de paramètre l.
    """
    return alea.expovariate(l)


def gauss(mu,sigma):
    """
    mu et sigma sont deux réels.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie un nombre réel choisi de manière aléatoire
    selon une loi nomale d'espérance mu et d'écart type sigma.
    """
    return alea.gauss(mu,sigma)

def normalFRep(a,b,mu,sigma):
    """
    a, b, mu et sigma sont quatre réels.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie une estimation de la probobilité P(a < X < b)
    lorsque X suit une loi normale d'espérance mu et d'écart type sigma.
    """
    if a < b :
        return norm.cdf(b,mu,sigma) - norm.cdf(a,mu,sigma)
    else :
        return 0

def invNorm(k,mu,sigma):
    """
    k, mu et sigma sont trois réels.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie la valeur du réel x telle que  P(X < x) = k
    lorsque X suit une loi normale d'espérance mu et d'écart type sigma.
    """
    return norm.ppf(k,mu,sigma)

def ajustement_affine(X, Y):
    """
    X et Y sont deux listes de nombre même taille
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Renvoie le couple (m,p) tel que y=mx+p soit l'ajustement affine de
    la série (X,Y) par méthode des moindres carrés.
    """
    m, p, _, _, _ = linregress(X,Y)
    return m, p