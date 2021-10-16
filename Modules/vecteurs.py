from math import *
import numpy as np
class vec():
    def vecteur(x,y,z='optionel'):
        if z=='optionel':
            return np.array([x,y])
        else :
            return np.array([x,y,z])

    def norme(v):
        l=v*v;n=0
        for i in range(len(l)) : n=n+l[i]
        return sqrt(n)

    def abscisse(v):
        return v[0]

    def ordonnee(v):
        return v[1]

    def cote(v):
        return v[2]


