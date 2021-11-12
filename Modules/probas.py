import math
import random

import matplotlib.pyplot as plt
import numpy as np
__version__ = '2.6'
pi=math.pi
AlphabetAP=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?&àâéèêëîïù#'(-_){}[]|\@=+°§$<>%*/"

# -------------------------------------------------------
#    FONCTIONS STAT & PROBAS
# -------------------------------------------------------
class probas():
    def choice(list):
        """
        list est une liste.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Renvoie un élément de la liste list choisi (pseudo)aléatoirement et de manière équipropable
        """
        return random.choice(list)

    def random():
        """
        Pas d'argument.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Renvoie au hasard un décimal de l'intervalle [0;1[
        """
        return random.random()

    def uniform(min,max):
        """
        min et max sont deux nombres.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Renvoie un nombre décimal choisi de manière (pseudo)aléatoire et
        uniforme de l'intervalle [min,max[.
        """
        return random.uniform(min,max)

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





    def uniform(min,max):
        """
        min et max sont deux nombres.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Renvoie un nombre décimal choisi de manière (pseudo)aléatoire et
        uniforme de l'intervalle [min,max[.
        """
        return random.uniform(min,max)

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
        return random.expovariate(l)


    def gauss(mu,sigma):
        """
        mu et sigma sont deux réels.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Renvoie un nombre réel choisi de manière aléatoire
        selon une loi nomale d'espérance mu et d'écart type sigma.
        """
        return random.gauss(mu,sigma)





