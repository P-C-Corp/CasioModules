# -*- coding: utf-8 -*-
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
from Modules.numpy import short
#import matplotlib.pyplot as plt
import numpy as np
__version__ = '2.6'
pi=math.pi
AlphabetAP=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?&àâéèêëîïù#'(-_){}[]|\@=+°§$<>%*/"





# -------------------------------------------------------
#    FONCTIONS STAT & PROBAS
# -------------------------------------------------------

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
#    FONCTIONS SUR NUMPY - stats
# -------------------------------------------------------




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
            list.append(random.randint(min,max))
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
            xi.short()
            ni.short()
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
"""
def quartile(xi,ni='optionnel',valeur='optionnel'):
    "
    xi est une série de valeurs
    ni est la série des effectifs associés (optionnelle)
    valeur est le quartile que l'on souhaite 1 ou 3 (optionnelle)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Retourne les quartiles de la liste.
    - Si valeur=1, retourne le premier quartile.
    - Si valeur=3, retourne le troisième quartile.
    - Par défaut, le premier et le troisième quartile sont retournés
    "
    if ni=='optionnel':                     #On vérifie si ni existe
        xi,ni=compte(xi,'effectif')
    elif ni==3 or ni==1:                    #On vérifie si valeur existe
        valeur=ni
        xi,ni=compte(xi,'effectif')
    else:                                   #ni existe, on vérifie si xi est ordonnée sinon on trie xi et ni
        if xi != sorted(xi) and type(ni)==list:
            xi.short()
            ni.short()
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
"""
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
            xi.short()
            ni.short()

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
    return math.sqrt(variance(xi,ni))


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





